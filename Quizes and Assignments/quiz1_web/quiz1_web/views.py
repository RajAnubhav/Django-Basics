from django.http import HttpResponse

def index(request):
    return HttpResponse("""
    This is the Main Page of this website <br>
    <ul>
        <li><a href="http://www.google.com", target="blank">Google</a></li>
        <li><a href="http://www.youtube.com", target="blank">Youtube</a></li>
        <li><a href="http://www.facebook.com", target="blank">Facebook</a></li>
        <li><a href="http://www.whatsapp.com", target="blank">Whatsapp</a></li>
        <li><a href="http://www.instagram.com", target="blank">Instagram</a></li>
    </ul> 
    """)