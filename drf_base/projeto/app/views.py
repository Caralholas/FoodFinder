# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import *
from serializers import *


@api_view(['GET'])
def foods_list(request):
    """
    List all foods
    """
    if request.method == 'GET':
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def new_food(request):
    """
    Create a new Food
    """
    if request.method == 'POST':
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_food(request, pk):
    """
    Get a specific food
    """
    if request.method == 'GET':
        try:
            food = Food.objects.get(pk=pk)
            serializer = FoodSerializer(food)
            return Response(serializer.data)
        except Food.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def restaurants_list(request):
    """
    List all restaurants
    """
    if request.method == 'GET':
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def new_restaurant(request):
    """
    Create a new Restaurant
    """
    if request.method == 'POST':
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_restaurant(request, pk):
    """
    Get a specific restaurant
    """
    if request.method == 'GET':
        try:
            restaurant = Restaurant.objects.get(pk=pk)
            serializer = RestaurantSerializer(restaurant)
            return Response(serializer.data)
        except Restaurant.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def restaurants_list_from_food(request, fk):
    """
    List all restaurants from specific food
    """
    if request.method == 'GET':
	foods = Food.objects.filter(name__icontains=fk)
	if foods.count == 1:
		try:
		    restaurant = Restaurant.objects.filter(foods=foods[0].id)
		    serializer = RestaurantSerializer(restaurant, many=True)
		    return Response(serializer.data)
		except Restaurant.DoesNotExist:
		    return Response(status=status.HTTP_404_NOT_FOUND)
	else:
		try:
		    restaurant = Restaurant.objects.filter(foods=1000000)
		    serializer = RestaurantSerializer(restaurant, many=True)
		    return Response(serializer.data)
		except Restaurant.DoesNotExist:
		    return Response(status=status.HTTP_404_NOT_FOUND) 
            

@api_view(['PUT'])
def update_restaurant(request, pk):
	if request.method == 'PUT':
		try:
			restaurant = Restaurant.objects.get(pk=pk)
			serializer = RestaurantSerializer(restaurant, data=request.data)
            
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(status=status.HTTP_400_BAD_REQUEST)
				
		except Restaurant.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

