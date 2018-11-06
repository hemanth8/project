from django.shortcuts import render
import json
from django.http import HttpResponse
import argparse
import pandas as pd
from .trial_recommend import TFIDF_MODEL
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

@api_view(['GET'])
def foo(request):
  '"testing ----------------------------\
  bnxs    bcdjfgwgfbbg fhfdfhdf fh dfhdhf d"'
  data = {
      "enabled": True,
      "action": "stage",
      "use_proxy": True,
      "ttl": 30,
      "fetch_frequency": 24,
      "host": "127.0.0.1",
      "access_key": 0,
      "min_severity": 1
      }
  return Response(data)

@api_view(['GET'])
def foo1(request):
  '"testing ----------------------------\
  bnxs    bcdjfgwgfbbg fhfdfhdf fh dfhdhf d"'
  data = {
      "enabled": True,
      "action": "stage",
      "use_proxy": True,
      "ttl": 30,
      "fetch_frequency": 24,
      "host": "127.0.0.1",
      "access_key": 0,
      "min_severity": 1
      }
  return Response(data)

recommend_model = TFIDF_MODEL()

def get_response_(query):
    indices = recommend_model.predict_obs(obs = query)
    return indices

@api_view(['GET'])
def get(self):
    query = "aws not working"
    indices = get_response_(query=query)
    data = pd.read_csv(r"C:\Users\Fission Labs\Downloads\processed_data.csv")
    data = data.sort_values(by='id')
    response = []
    for ind in indices:
        response.append(dict(data.iloc[ind]))
    print(response,"get")
    return Response(response)


class Index(APIView):
    def get(self, request, format=None):

        """Build a list of all established API endpoints, expects either a Router
        or an API view named 'index' to be in the module.
        """

        data = {"message":"success"}
        return Response(data)



