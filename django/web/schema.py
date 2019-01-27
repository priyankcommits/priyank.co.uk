from web.models import Profile, Post, Article, Subscribers
from web.utils import get_post_likes, post_like, create_subscriber

import graphene
from graphene import ObjectType, Node, Schema, InputObjectType, relay
from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType
from graphql_relay.node.node import from_global_id


class ProfileNode(DjangoObjectType):

    class Meta:
        model = Profile
        interfaces = (Node, )


class PostNode(DjangoObjectType):

    class Meta:
        model = Post
        interfaces = (Node, )


class ArticleNode(DjangoObjectType):

    class Meta:
        model = Article
        interfaces = (Node, )


class PostUpdateFields(InputObjectType):
    slug = graphene.String(required=True)


class PostUpdate(relay.ClientIDMutation):
    class Input:
        post = graphene.Argument(PostUpdateFields)

    update = graphene.Field(PostNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, post):
        try:
            post_slug = post['slug']
            post = Post.objects.get(slug=post_slug)
            post_like(post_slug, post.likes+1)
            return PostUpdate(udpate=post)
        except:
            return PostUpdate(update=None)


class SubscribersNode(DjangoObjectType):

    class Meta:
        model = Subscribers
        interfaces = (Node, )


class SubscriberFields(InputObjectType):
    name = graphene.String(required=True)
    email = graphene.String(required=True)


class SubscribersCreate(relay.ClientIDMutation):
    class Input:
        subscriber = graphene.Argument(SubscriberFields)

    create = graphene.Field(SubscribersNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, subscriber):
        try:
            create_subscriber(subscriber['name'], subscriber['email'])
            subscriber = Subscribers.objects.get_or_create(
                name=subscriber['name'], email=subscriber['email'])
            return SubscribersCreate(create=subscriber)
        except:
            return SubscribersCreate(create=None)


class Mutation(ObjectType):
    update = PostUpdate.Field()
    create = SubscribersCreate.Field()


class Query(ObjectType):
    profile = Node.Field(ProfileNode)
    all_profiles = DjangoConnectionField(ProfileNode)

    slug_post = graphene.Field(PostNode, slug=graphene.String())
    all_posts = DjangoConnectionField(PostNode)

    def resolve_all_posts(self, info, **kwargs):
        posts = Post.objects.all().order_by('-created')
        post_likes = get_post_likes()
        for post in posts:
            post.likes = post_likes.get(post.slug, 0)
        return posts

    def resolve_slug_post(self, info, **kwargs):
        return Post.objects.get(slug=kwargs['slug'])

    article = Node.Field(ArticleNode)
    all_articles = DjangoConnectionField(ArticleNode)

schema = Schema(query=Query, mutation=Mutation)
