from django.db import models


class QuoteAnalysis(models.Model):
    quote = models.TextField(unique=True)
    total_letters = models.PositiveIntegerField()
    total_vowel_letters = models.PositiveIntegerField()
    total_consonant_letters = models.PositiveIntegerField()
    total_similar_letters = models.JSONField()
    average_word_len = models.PositiveIntegerField()
    top_three_words = models.JSONField()
    
