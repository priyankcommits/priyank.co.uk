from web.models import Profile, Post, Article, Subscribers
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
    id = graphene.String(required=True)


class PostUpdate(relay.ClientIDMutation):
    class Input:
        post = graphene.Argument(PostUpdateFields)

    update = graphene.Field(PostNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, post):
        try:
            post = Post.objects.get(id=from_global_id(post['id'])[1])
            post.likes += 1
            post.save()
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

    post = Node.Field(PostNode)
    all_posts = DjangoConnectionField(PostNode)

    article = Node.Field(ArticleNode)
    all_articles = DjangoConnectionField(ArticleNode)

schema = Schema(query=Query, mutation=Mutation)
