from django.db import models
from django.utils import timezone


class Post(models.Model): #models.Modelはdjangoが呼ぶ固有名詞　”これがデータベースに保存すべき”だと認識するもの
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)#models.foreignkey他のモデルへのリンク
    title = models.CharField(max_length=200)#models.charfield文字数が制限されたフィールド
    text = models.TextField()#models.textfield制限なしのフィールド
    created_date = models.DateTimeField(
            default=timezone.now)#models.datetimefield日付と時間のフィールド
    published_date = models.DateTimeField(
            blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title