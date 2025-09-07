from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from projects.models import Project, TeamMember
from .forms import ProfileUpdateForm, CustomPasswordChangeForm

User = get_user_model()

# -------- API-based views --------

@api_view(["POST"])
@permission_classes([AllowAny])
def api_register(request):
    """Register a new user"""
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework_simplejwt.tokens import RefreshToken

@api_view(["POST"])
@permission_classes([AllowAny])
def api_login(request):
    """Login user and return JWT tokens"""
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(request, username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            "message": "Login successful",
            "username": user.username,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }, status=status.HTTP_200_OK)

    return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)




@api_view(["POST"])
@permission_classes([IsAuthenticated])
def api_logout(request):
    """Client should delete their token to 'logout'"""
    return Response({"message": "Logout successful"})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def api_dashboard(request):
    """Simple dashboard response"""
    user = request.user
    return Response({"message": f"Welcome {user.username}, this is your dashboard!"})


@api_view(["GET", "PUT"])
@permission_classes([IsAuthenticated])
def api_profile(request):
    """Get or update user profile"""
    if request.method == "GET":
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def api_change_password(request):
    """Change password"""
    password_form = CustomPasswordChangeForm(user=request.user, data=request.data)

    if password_form.is_valid():
        user = password_form.save()
        update_session_auth_hash(request, user)  # keep user logged in after password change
        return Response({"message": "Password changed successfully"})
    return Response(password_form.errors, status=status.HTTP_400_BAD_REQUEST)
