from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models import Q

def equijoin(request):
    EQUIOBJECT=Emp.objects.select_related('deptno').all()   #it is used for joining
    EQUIOBJECT=Emp.objects.select_related('deptno').filter(MGR__isnull=True)
    EQUIOBJECT=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    EQUIOBJECT=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    EQUIOBJECT=Emp.objects.select_related('deptno').filter(hiredate__year=2022)
    EQUIOBJECT=Emp.objects.select_related('deptno').filter(sal__gt=2800) #greater than 2800
    EQUIOBJECT=Emp.objects.select_related('deptno').filter(sal__lt=2800)  #less than 2800
    EQUIOBJECT=Emp.objects.select_related('deptno').filter(deptno__dname='SALES')
    EQUIOBJECT=Emp.objects.select_related('deptno').filter(deptno__dloc='NEW YORK')
    EQUIOBJECT=Emp.objects.select_related('deptno').filter(deptno=20)
    EQUIOBJECT=Emp.objects.select_related('deptno').filter(ename='JONES')
    EQUIOBJECT=Emp.objects.select_related('deptno').filter(job='MANAGER',deptno=20,sal__gt=1800)
    EQUIOBJECT=Emp.objects.select_related('deptno').filter(ename='JONES')
    EQUIOBJECT=Emp.objects.select_related('deptno').filter(deptno__dname='SALES')
    EQUIOBJECT=Emp.objects.select_related('deptno').all()[:5:]
    EQUIOBJECT=Emp.objects.select_related('deptno').all()[1:5:]
    EQUIOBJECT=Emp.objects.select_related('deptno').filter(deptno__dloc='NEW YORK')
    d={'EQUIOBJECT':EQUIOBJECT}
    return render(request,'equijoin.html',d)



def selfjoin(request):
    empmgrobj=Emp.objects.select_related('MGR').all()
    empmgrobj=Emp.objects.select_related('MGR').filter(sal__gt=2800)
    empmgrobj=Emp.objects.select_related('MGR').filter(MGR__ename='KING')
    empmgrobj=Emp.objects.select_related('MGR').filter(sal=2500)
    empmgrobj=Emp.objects.select_related('MGR').filter(sal__lt=2500)
    empmgrobj=Emp.objects.select_related('MGR').filter(MGR__sal=2500)
    empmgrobj=Emp.objects.select_related('MGR').filter(hiredate__year=2022)
    empmgrobj=Emp.objects.select_related('MGR').filter(hiredate__gt='2022-10-20')
    empmgrobj=Emp.objects.select_related('MGR').filter(hiredate__lt='2022-10-20')
    empmgrobj=Emp.objects.select_related('MGR').filter(MGR__hiredate__year=2022)
    empmgrobj=Emp.objects.select_related('MGR').filter(ename__startswith='K')
    empmgrobj=Emp.objects.select_related('MGR').filter(ename__endswith='G')
    empmgrobj=Emp.objects.select_related('MGR').filter(MGR__sal__lt=2500)
    empmgrobj=Emp.objects.select_related('MGR').filter(ename='ALLEN')
    empmgrobj=Emp.objects.select_related('MGR').filter(ename__startswith='B',sal__gt=2500)
    empmgrobj=Emp.objects.select_related('MGR').filter(MGR__ename__startswith='K')
    empmgrobj=Emp.objects.select_related('MGR').filter(ename='BLAKE',sal=2850)
    empmgrobj=Emp.objects.select_related('MGR').filter(ename__endswith='E',sal__gt=2500,ename='BLAKE')
    d={'empmgrobj':empmgrobj}
    return render(request,'selfjoin.html',d)
    




def emp_mgr_dept(request):
    emd=Emp.objects.select_related('deptno','MGR').all()
    emd=Emp.objects.select_related('deptno','MGR').filter(deptno__dname='RESEARCH')
    emd=Emp.objects.select_related('deptno','MGR').filter(MGR__ename='JONES')
    emd=Emp.objects.select_related('deptno','MGR').filter(deptno__dname='RESEARCH',MGR__ename='JONES')
    emd=Emp.objects.select_related('deptno','MGR').filter(deptno__dname='SALES',MGR__ename='BLAKE',ename='MARTIN')
    emd=Emp.objects.select_related('deptno','MGR').filter(ename='ALLEN')
    emd=Emp.objects.select_related('deptno','MGR').filter(deptno__dname='RESEARCH')
    emd=Emp.objects.select_related('deptno','MGR').filter(Q(deptno__dname='RESEARCH')|Q(MGR__ename='BLAKE'))
    emd=Emp.objects.select_related('deptno','MGR').filter(Q(deptno__dname='RESEARCH')|Q(MGR__ename='BLAKE') |Q(deptno__dname='SALES'))
    emd=Emp.objects.select_related('deptno','MGR').filter(ename__endswith='G')
    emd=Emp.objects.select_related('deptno','MGR').filter(ename__startswith='B')
    emd=Emp.objects.select_related('deptno','MGR').filter(MGR__ename__endswith='G')
    emd=Emp.objects.select_related('deptno','MGR').filter(ename__endswith='N',ename__startswith='A')
    emd=Emp.objects.select_related('deptno','MGR').filter(Q(ename__endswith='N') |Q(ename__startswith='A'))
    emd=Emp.objects.select_related('deptno','MGR').filter(Q(ename__endswith='N') |Q(ename__startswith='A') |Q(sal__gt=1000))
    emd=Emp.objects.select_related('deptno','MGR').filter(ename__endswith='E',sal__gt=3000,ename='BLAKE')
    emd=Emp.objects.select_related('deptno','MGR').filter(Q(ename__endswith='E')| Q(sal__gt=3000) |Q(ename='BLAKE'))
    emd=Emp.objects.select_related('deptno','MGR').filter(ename__endswith='T',sal__gte=3000,deptno__dname='RESEARCH')
    emd=Emp.objects.select_related('deptno','MGR').filter(hiredate__year=2022)
    emd=Emp.objects.select_related('deptno','MGR').filter(MGR__hiredate__year=2022)
    emd=Emp.objects.select_related('deptno','MGR').filter(MGR__hiredate__year=2022,hiredate__year=2022)
    emd=Emp.objects.select_related('deptno','MGR').all()[:5:]
    emd=Emp.objects.select_related('deptno','MGR').all()[3::]
    emd=Emp.objects.select_related('deptno','MGR').filter(Q(MGR__hiredate__year=2022)|Q(hiredate__year=2021))
    emd=Emp.objects.select_related('deptno','MGR').filter(sal__gt=3000)
    emd=Emp.objects.select_related('deptno','MGR').filter(deptno__dname='RESEARCH',MGR__ename='KING',ename='JONES')
    emd=Emp.objects.select_related('deptno','MGR').filter(Q(deptno__dname='RESEARCH')|Q(MGR__ename='ALLEN')|Q(ename='JONES'))
    emd=Emp.objects.select_related('deptno','MGR').filter(Q(deptno__dname='RESEARCH')|Q(MGR__ename='KING')|Q(ename='JONES')|Q(MGR__sal__gte=3000))
    emd=Emp.objects.select_related('deptno','MGR').filter(sal__gt=3000,comm__isnull=True)
    emd=Emp.objects.select_related('deptno','MGR').filter(deptno__dloc='NEW YORK')
    emd=Emp.objects.select_related('deptno','MGR').filter(Q(deptno__dloc='NEW YORK')| Q(deptno__deptno=20)| Q(deptno__dname='RESEARCH'))
    emd=Emp.objects.select_related('deptno','MGR').filter(comm__isnull=True,MGR__isnull=True,sal__gt=3000)
    emd=Emp.objects.select_related('deptno','MGR').filter(deptno__dloc='NEW YORK',deptno__deptno=20,deptno__dname='RESEARCH')
    emd=Emp.objects.select_related('deptno','MGR').filter(deptno__dloc='DALLAS',deptno__deptno=20,deptno__dname='RESEARCH')
    emd=Emp.objects.select_related('deptno','MGR').filter(comm__isnull=True,MGR__isnull=True)
    emd=Emp.objects.select_related('deptno','MGR').filter()
    emd=Emp.objects.select_related('deptno','MGR').all()[::-1]
    emd=Emp.objects.select_related('deptno','MGR').filter(Q(empno=7788)|Q(ename='KING'))
    emd=Emp.objects.select_related('deptno','MGR').filter(empno=7839,ename='KING',sal__gt=3000)
    d={'emd':emd}
    return render(request,'emp_mgr_dept.html',d)




def emp_salgrade(request):
    EO=Emp.objects.all()
    SO=SalGrade.objects.all()


    SO=SalGrade.objects.filter(grade=5)
    EO=Emp.objects.filter(sal__range=(SO[0].losal,SO[0].hisal))


    SO=SalGrade.objects.filter(grade__in=(3,4))
    EO=Emp.objects.none()   #to create empty queryset[]
    for sgo in SO:
        EO=EO|Emp.objects.filter(sal__range=(sgo.losal,sgo.hisal))



    SO=SalGrade.objects.filter(grade__in=(4,5))
    EO=Emp.objects.none()   
    for sgo in SO:
        EO=EO|Emp.objects.filter(sal__range=(sgo.losal,sgo.hisal))
    


    SO=SalGrade.objects.filter(grade__in=(4,5))
    EO=Emp.objects.none()  
    for sgo in SO:
        EO=EO|Emp.objects.filter(sal__range=(sgo.losal,sgo.hisal),ename='SCOTT') 
    
    d={'EO':EO ,'SO':SO}
    return render(request,'emp_salgrade.html',d)
    
















                                                                                                            

   

   




    



    

    
   

    


    
