# from rest_framework.views import APIView
# from rest_framework import permissions
# from rest_framework.response import Response
# from post.models import Article as ArticleModel


# class ArticleView(APIView):  # CBV 방식

#     # permission_classes = [permissions.AllowAny]  # 누구나 view 조회 가능
#     # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
#     # permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능

#     # 로그인 한 사용자의 게시글 목록 return
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request):
#         user = request.user

#         articles = ArticleModel.objects.filter(user=user)
#         titles = [article.title for article in articles]  # list 축약 문법

#         # titles = []

#         # for article in articles:
#         #     titles.append(article.title)

#         return Response({"article_list": titles})
