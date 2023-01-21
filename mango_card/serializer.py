from rest_framework import serializers
from .models import Mango, Comments


class MangoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mango
        fields = 'title photo released'.split()


class MangoDetailSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    genre = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Mango
        fields = 'title photo info released type genre description comments'.split()

    def get_genre(self, mango):
        return [i.title for i in mango.genre.all()]

    def get_type(self, mango):
        return mango.type.title

    def get_comments(self, manga):
        answer = []
        for i in manga.comment.all():
            acc_lst = {"photo": f"http://127.0.0.1:8000/{i.author.photo.url}",
                       "username": i.author.username,
                       "nickname": i.author.nickname, "text": i.text}
            answer.append(acc_lst)
        return answer


class MangoCommentsSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Mango
        fields = "comments".split()

    def get_comments(self, manga):
        answer = []
        for i in manga.comment.all():
            acc_lst = {"photo": f"http://127.0.0.1:8000/{i.author.photo.url}",
                       "username": i.author.username,
                       "nickname": i.author.nickname, "text": i.text}
            answer.append(acc_lst)
        return answer


class CommentsSerializer(serializers.ModelSerializer):
    mango = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()

    class Meta:
        model = Comments
        fields = "author mango text".split()

    def get_mango(self, comment):
        return comment.book.title

    def get_author(self, comment):
        acc = {
            "username": comment.author.username,
            "nickname": comment.author.nickname
        }
        return acc


class CommentCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating a new Comment model instances."""
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comments
        fields = 'id author mango text'.split()
        read_only_fields = "id mango".split()
