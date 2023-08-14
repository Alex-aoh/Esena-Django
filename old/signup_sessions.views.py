# --- SignUp Session Username ---
# - GET -> SignUp Session Username Check -> REQ: USERNAME IN JSON -> RET: SESSION ID AND USERNAME RESPONSE
# - POST -> SignUp Session Username Update -> REQ: USERNAME IN JSON -> RET: SESSION ID AND USERNAME RESPONSE
# class SignUpSessionUsername(APIView):
#     """
#     Check or Update username in SignUp Session.
#     Get -> Check Username
#     Post -> Update Username
#     * Only authenticated users are able to access this view.
#     """
#     authentication_classes = []
#     permission_classes = [permissions.IsAuthenticated]
    

#     # Check Username avaiilabity
#     def get(self, request, format=None, *args, **kwargs):
#         """
#         Return a list of all users.
#         """
#         auth0user = request.user.auth0user
#         serializer = UsernameSerializer(data=request.data)  
        
#         if serializer.is_valid():
#             username = serializer.validated_data['username']
#             try:
#                 check_result = username_signup_session_check(auth0user=auth0user, username=username)
#             except ServiceUnavailable:
#                 raise ServiceUnavailable(detail="Can't check the username availability, try again later.")
#             else:
#                 return Response({"username": username, "used": check_result})
#         else:
#             raise exceptions.ParseError(detail="Not username in json body.")
#     def post(self, request, format=None):
#         auth0user = request.user.auth0user
#         serializer = UsernameSerializer(data=request.data)  

#         if serializer.is_valid():
#             username = serializer.validated_data['username']
#             try:
#                 check_result = username_signup_session_update(auth0user=auth0user, username=username)
#             except ServiceUnavailable:
#                 raise ServiceUnavailable(detail="Can't check the username availability, try again later.")
#             else:
#                 return Response({"username": username, "used": check_result})
#         else:
#             raise exceptions.ParseError(detail="Not username in json body.")

#         # try: 
#         #     serializer.is_valid()
#         # except JSONDecodeError:
#         #     raise exceptions.ParseError(detail="Body is not json.")
#         # else:
#         #     try:
#         #         username = serializer.validated_data["username"]
#         #     except KeyError:
#         #         raise exceptions.ParseError(detail="Not username in json body.")
#         #     else:
#         #         try:
#         #             check_result = username_signup_session_check(auth0user=auth0user, username=username)
#         #         except ServiceUnavailable:
#         #             raise ServiceUnavailable(detail="Can't check the username availability, try again later.")
#         #         else:
#         #             return Response({"username": username, "used": check_result})
#     # def post(self, request, format=None): 
