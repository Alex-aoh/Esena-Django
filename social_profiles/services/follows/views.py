from rest_framework import viewsets, views, permissions, status
from rest_framework.response import Response
from social_profiles.models import SocialProfile
from .serializers import BlockPendingSerializer, FollowerSerializer, SocialProfile


#TO-DO: Add check of ids and type in request

class FollowUnfollowView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def func_get_profile(self,pk):
        try:
            return SocialProfile.objects.get(id=pk)
        except SocialProfile.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND # Http404
        
    def func_check_legit(self, request, current_id):
        legit = False
        account = request.user.auth0user.account
        account_sps = SocialProfile.objects.filter(account=account)
        for sp in account_sps.iterator():
            if str(sp.id) == (current_id):
                legit = True
                break
        return legit
    
    # Here we manage all the requests for follow, unfollow, accept, decline, remove_request(cancel the request sended) and remove
    def post(self, request,format=None):   
        current_id = request.data.get('id')
        other_id = request.data.get('other_id')
        req_type = request.data.get('type') 

        #TO-DO: Add check of ids and type in request
        #TO-DO: Check is not my id
        # Check if the user sending the request is owner of the SP
        if self.func_check_legit(request=request, current_id=current_id) == False:
            return Response({"error": "Your passing another id. It need to be your id."},status=status.HTTP_406_NOT_ACCEPTABLE)
        # End of Check
        
        if current_id == other_id:
            return Response({"error": "Your passing your id. It need to be a diferent id."},status=status.HTTP_406_NOT_ACCEPTABLE)  
        current_profile = self.func_get_profile(current_id)
        other_profile = self.func_get_profile(other_id)

        if req_type == 'follow':
            if other_profile.private_profile:
                other_profile.pending_request.add(current_profile)
                return Response({"Requested" : "Follow request has been send!!"},status=status.HTTP_200_OK)
            else:
                if other_profile.blocked_user.filter(id = current_profile.id).exists():
                    return Response({"Following Fail" : "You can not follow this profile becuase your ID blocked by this user!!"},status=status.HTTP_400_BAD_REQUEST)
                current_profile.following.add(other_profile)
                other_profile.followers.add(current_profile)
                return Response({"Following" : "Following success!!"},status=status.HTTP_200_OK) 
            
        elif req_type == 'remove_request':
            other_profile.pending_request.remove(current_profile)
            return Response({"Remove Request" : "Follow request successfully removed!!"},status=status.HTTP_200_OK)
        
        elif req_type == 'accept':
            current_profile.followers.add(other_profile)
            other_profile.following.add(current_profile)
            current_profile.pending_request.remove(other_profile)
            return Response({"Accepted" : "Follow request successfuly accespted!!"},status=status.HTTP_200_OK)
            
        elif req_type == 'decline':
            current_profile.pending_request.remove(other_profile)
            return Response({"Decline" : "Follow request successfully declined!!"},status=status.HTTP_200_OK)
            
        elif req_type == 'unfollow':
            current_profile.following.remove(other_profile)
            other_profile.followers.remove(current_profile)
            return Response({"Unfollow" : "Unfollow success!!"},status=status.HTTP_200_OK)
                
        elif req_type == 'remove':     # You can remove your follower
            current_profile.followers.remove(other_profile)
            other_profile.following.remove(current_profile)
            return Response({"Remove Success" : "Successfuly removed your follower!!"},status=status.HTTP_200_OK)
        
        else:
            return Response({"error": "Incorrect type"},status=status.HTTP_406_NOT_ACCEPTABLE)
     

    # Here we can fetch followers,following detail and blocked user,pending request,sended request.. 
    # TO-DO: This views is for the user sending the request. Create a view showing the follow_detail to anyone??
    def patch(self, request,format=None):

        current_id = request.data.get('id')
        req_type = request.data.get('type')
        
        #TO-DO: Add check of ids and type in request

        # Check if the user sending the request is owner of the SP
        if self.func_check_legit(request=request, current_id=current_id) == False:
            return Response({"error": "Your passing another id. It need to be your id."},status=status.HTTP_406_NOT_ACCEPTABLE)
        # End of Check


        current_profile = self.func_get_profile(current_id)

        #Follow Detail Followers, Following
        if req_type == 'follow_detail':
            serializer = FollowerSerializer(current_profile)
            return Response({"data" : serializer.data},status=status.HTTP_200_OK)
        
        #Blocked users, Pending requests, and Sended Requests
        elif req_type == 'block_pending':
            serializer = BlockPendingSerializer(current_profile)
            pf = list(SocialProfile.objects.filter(pending_request = current_profile.id).values('id','username'))
            return Response({"data" : serializer.data,"Sended Request" :pf},status=status.HTTP_200_OK)  
        
        else:
            return Response({"error": "Incorrect type"},status=status.HTTP_406_NOT_ACCEPTABLE) 
        
    # You can block and unblock user
    def put(self, request,format=None):

        current_id = request.data.get('id')
        other_id = request.data.get('other_id')           
        req_type = request.data.get('type')

        #TO-DO: Add check of ids and type in request
        
        # Check if the user sending the request is owner of the SP
        if self.func_check_legit(request=request, current_id=current_id) == False:
            return Response({"error": "Your passing another id. It need to be your id."},status=status.HTTP_406_NOT_ACCEPTABLE)
        # End of Check
        
        if current_id == other_id:
            return Response({"error": "Your passing your id. It need to be a diferent id."},status=status.HTTP_406_NOT_ACCEPTABLE)  
        current_profile = self.func_get_profile(current_id)
        other_profile = self.func_get_profile(other_id)

        current_profile = self.func_get_profile(current_id)
        other_profile = self.func_get_profile(other_id)

        # Block User
        if req_type == 'block':
            current_profile.followers.remove(other_profile)
            current_profile.following.remove(other_profile)
            other_profile.followers.remove(other_profile)
            other_profile.following.remove(other_profile)
            current_profile.blocked_user.add(other_profile)
            return Response({"Blocked" : "This user blocked successfuly"},status=status.HTTP_200_OK)
        elif req_type == 'unblock':
            current_profile.blocked_user.remove(other_profile)
            return Response({"Unblocked" : "This user unblocked successfuly"},status=status.HTTP_200_OK)
