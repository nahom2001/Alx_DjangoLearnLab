from django.core.exceptions import PermissionDenied

def role_required(allowed_roles=[]):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if hasattr(request.user, 'profile') and request.user.profile.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return _wrapped_view
    return decorator
