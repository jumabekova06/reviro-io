import json
from rest_framework import viewsets
from .serializers import QuoteSerializer
from .models import QuoteAnalysis
from .scraping import *
import asyncio



class QuoteSaveView(viewsets.ModelViewSet):
 
    serializer_class = QuoteSerializer

    def get_queryset(self):
        result = []
        test1=asyncio.run(main())
        for data in test1:
            
            if QuoteAnalysis.objects.filter(quote=data).exists():

                resp=QuoteAnalysis.objects.get(quote=data)
                result.append(resp)
            else:
                quote_analysis = {}
                vowel_and_consonant = total_vowel_and_consonant_letters(data)
                quote_analysis['quote'] = data
                quote_analysis['total_letters'] = total_letters(data)
                quote_analysis['total_vowel_letters'] = vowel_and_consonant['vowels_count']
                quote_analysis['total_consonant_letters'] = vowel_and_consonant['consonant_count']
                quote_analysis['total_similar_letters'] = json.dumps(total_similar_letter(data))
                quote_analysis['average_word_len'] = average_word_len(data)
                quote_analysis['top_three_words'] = json.dumps(get_top_length_word(data))
                result.append(quote_analysis)
                QuoteAnalysis.objects.create(**quote_analysis)
        
        print(len(result),'не могу понять почему он 2 раза парсинг делает')
        return result