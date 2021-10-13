from django.db import models

# Create your models here.
class Topic(models.Model):
    """使用类（属性+方法）来定义用户学习的主题"""
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回self中（模型中）的字符串表示"""
        return self.text

class Entry(models.Model):
    """使用户能过对每一个主题进行进一层级地具体描述"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."