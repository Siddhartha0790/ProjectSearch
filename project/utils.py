from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def pagination(request,projects):
    
    Page=1
    size=3
    paginator = Paginator(projects,size)
    newprojects =projects 
    if request.GET.get('page'):
        try:
            Page = request.GET.get('page')
            newprojects = paginator.page(Page)
        except EmptyPage:
            Page = 1
            newprojects = paginator.page(Page)
        except PageNotAnInteger:
            Page=1
            newprojects = paginator.page(Page)
            
    left_range= int(Page)-2
    
    if left_range < 1:
        left_range=1
        
        
    right_range = int(Page)+2
    
    if right_range > paginator.num_pages:
        right_range = paginator.num_pages +1
    
    custom_range = range(left_range , right_range)
    
    return custom_range,newprojects