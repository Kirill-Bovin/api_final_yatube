from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from posts.models import Group, Post

from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет получения, записи и изменения постов."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Метод создания нового поста."""
        return serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет получения данных групп пользователей."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthorOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет получения, записи и изменения комментариев."""
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        """Метод отображения всех комментариев."""
        post = self.__get_post()
        return post.comments.all()

    def perform_create(self, serializer):
        """Метод создания нового комментария."""
        post = self.__get_post()
        serializer.save(author=self.request.user, post=post)

    def __get_post(self):
        """Метод получения поста по id."""
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Вьюсет получения подписок."""
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username',)

    def get_queryset(self):
        """Метод отображения подписок."""
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        """Метод создания подписки"""
        serializer.save(user=self.request.user)
