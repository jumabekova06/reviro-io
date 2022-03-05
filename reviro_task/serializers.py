from rest_framework import serializers

from .models import QuoteAnalysis

class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuoteAnalysis
        
        fields = (
            'quote',
            'total_letters',
            'total_vowel_letters',
            'total_consonant_letters',
            'total_similar_letters',
            'average_word_len',
            'top_three_words'
        )
