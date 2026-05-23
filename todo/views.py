from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Todo
from .serializers import TodoSerializer


class TodoListCreateAPIView(APIView):
    def get(self, request, user_id):
        todos = Todo.objects.filter(user_id=user_id)

        serializer = TodoSerializer(todos, many=True)

        return Response(serializer.data)

    def post(self, request, user_id):
        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user_id=user_id)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailAPIView(APIView):
    def get_object(self, user_id, pk):
        try:
            return Todo.objects.get(user_id=user_id, pk=pk)
        except Todo.DoesNotExist:
            return None

    def get(self, request, user_id, pk):
        todo = self.get_object(user_id, pk)

        if not todo:
            return Response(
                {"detail": "Todo not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = TodoSerializer(todo)

        return Response(serializer.data)

    def put(self, request, user_id, pk):
        todo = self.get_object(user_id, pk)

        if not todo:
            return Response(
                {"detail": "Todo not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = TodoSerializer(todo, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, pk):
        todo = self.get_object(user_id, pk)

        if not todo:
            return Response(
                {"detail": "Todo not found"}, status=status.HTTP_404_NOT_FOUND
            )

        todo.delete()

        return Response({"detail": "Todo deleted"}, status=status.HTTP_204_NO_CONTENT)