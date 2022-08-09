option=int(input("Enter your option\n1.Circle\n2.Triangle\n3.Rectangle\n4.Square\n5.sphere\n6.Cylinder\n7.Parallelogram\n8.Cube\n9.Pentagon\n10.cone:-"))

if option==1:
	calc=int(input("what do you want to calculate\n1.Area\n2.Diameter\n3.Circumference\n4.chord\n5.Arc:-"))
	radius=int(input("Enter radius of circle:-"))
	if calc==1:
		a=22/7*radius*radius
		print("Area of the circle:",a)
	elif calc==2:
		      b=2*radius
		      print("Diameter of the circle:",b)
	elif calc==3:
		c=2*22/7*radius
		print("Circumference of the Circle:",c)	      
if option==2:
	calc=int(input("what do you want to calculate\n1.Area\n2.Hight\n3.Base\n4.Parimeter:-"))
	if calc==1:
		Hight=int(input("Enter the hight of triangle:-"))
		Base=int(input("Enter the base of triangle:-"))
		print("The area of the given Triangle:",1/2*Hight*Base)
	elif calc==2:
	   	Area=int(input("Enter the Area of triangle:-"))
	   	Base=int(input("Enter the Base of triangle"))
	   	print("The hight of the given triangle:",Area*2/Base)
	elif calc==3:
	  	Area=int(input("Enter the Area of triangle:-"))
	  	Hight=int(input("Enter the Hight of triangle:-"))
	  	print("The Base of the given triangle:",Area*2/Hight)
	elif calc==4:
			Hight=int(input("Enter the Hight of triangle:-"))
			Base=int(input("Enter the Base of triangle:-")) 
			hypotenuse=int(input("Enter the hypotenuse of triangle:-"))
			print("The parameter of the given triangle:",Hight+Base+hypotenuse)

if option==3:
							calc=int(input("what do you want to calculate\n1.Length\n2.Breth\n3.Area\n4.Premeter:-"))
							if calc==1:
								Area=int(input("Enter the Area of rectangle:-"))
								Breth=int(input("Enter the breath of rectangle:-"))
								l=Area/Breth
								print("The length of the given rectangle:",l)
							elif calc==2:
								Area=int(input("Enter the Area of rectangle:-"))
								length=int(input("Enter the length of rectangle:-"))
								b=Area/length
								print("The breth of given rectangle:",b)
							elif calc==3:
								length=int(input("Enter the length of rectangle:-"))
								breth=int(input("Enter the breth of rectangle:-"))
								A=length*breth
								print("The Area of given rectangle:",A)
							elif calc==4:
								length=int(input("Enter the length of rectangle:-"))
								breth=int(input("Enter the breth of rectangle:-"))
								P=1/2*length+breth
								print("The premeter of the given rectangle:",P)
								
if option==4:
	calc=int(input("What do you want to calculate\n1.Area\n2.Perimeter:-"))
	if calc==1:
		a=int(input("Enter the a of squre:-"))
		A=a*a
		print("The Area of given squre:",A)
	elif calc==2:
		Area=int(input("Enter the Area of squre"))
		P=4*Area
		print("The Perimeter of squre:",P)
		
if option==5:
			calc=int(input("what do you want to calculate\n1.Diameter\n2.Area\n3.Volume:-"))
			if calc==1:
				radius=int(input("Enter the radius of sphere:-"))
				D=2*radius
				print("The diameter of the given sphere:",D)
			elif calc==2:
				radius=int(input("Enter the radius of sphere:-"))
				A=4*22/7*radius*radius
				print("The Area of the given sphere:",A)
			elif calc==3:
				radius=int(input("Enter the radius of sphere:-"))
				V=4/3*22/7*radius*radius*radius
				print("The volume of the given sphere:",V)
				
if option==6:
						calc=int(input("what do you want to calculate\n1.Curved surface Area\n2.Total surface Area\n3.Volume\n4.Hight"))
						if calc==1:
							radius=int(input("Enter the radius of cylinder:-"))
							Hight=int(input("Enter the Hight of Cylinder"))
							C=2*22/7*radius*Hight
							print("The curved surface Area of cylinder:",C)
						elif calc==2:
							radius=int(input("Enter the radius of cylinder:-"))
							hight=int(input("Enter the hight of cylinder:-"))
							T=2*22/7*radius*hight+2*22/7*radius*radius
							print("The total surface Area of cylinder:",T)	
						elif calc==3:
							radius=int(input("Enter the radius of cylinder:-"))
							hight=int(input("Enter the hight of cylinder"))
							V=22/7*radius*radius*hight
							print("The volume of Cylinder:",V)
						elif calc==4:
							radius=int(input("Enter the radius of cylinder:-"))
							Volume=int(input("Enter the Volume of cylinder:-"))
							H=Volume*7/22*radius*radius
							print("The Hight of the cylinder:",H)
			
if option==7:
	calc=int(input("what do you want to calculate\n1.Area\n2.Hight\n3.Base:-"))
	if calc==1:
		Base=int(input("Enter the Base of Parellelogram:-"))
		Hight=int(input("Enter the Hight of Parellelogram:-"))
		A=Base*Hight
		print("The Area of Parellelogram:",A)
	elif calc==2:
	   		Area=int(input("Enter the Area of parellelogram:-"))
	   		Base=int(input("Enter the Base of parellelogram:-"))
	   		H=Area/Base
	   		print("The Higjt of parellelogram:",H)
	elif calc==3:
	   		Area=int(input("Enter the Area of parellelogram:-"))
	   		Hight=int(input("Enter the Hight of parellelogram"))
	   		B=Area/Hight
	   		print("The Base of Parellelogram:",B)

if option==8:
	calc=int(input("what do you want calculate\n1.Total Surface Area\n2.leteral surface Area\n3.Volume:-"))
	if calc==1:
	   			   		side=int(input("Enter the side of cube:-"))
	   			   		S=6*side*side
	   			   		print("The total surface of cube:",S)
	elif calc==2:
	   			   		side=int(input("Enter the side of cube"))
	   			   		F=4*side*side
	   			   		print("The leteral surface area:",F)
	elif calc==3:
		side=int(input("Enter the side of cube"))
		V=side*side*side
		print("The Volume of Cube:",V)
		
if option==9:
	calc=int(input("What do you want to calculate\n1.Area\n2.perimeter\n3.length"))
	if calc==1:
		perimeter=int(input("Enter the perimeter of pentagon:-"))
		length=int(input("Enter the length of pentagon:-"))
		A=5/2*perimeter*length
		print("The Area of Pentagon:",A)
	elif calc==2:
				  			   		  			   			Area=int(input("Enter the Area of pentagon:-"))
				  			   		  			   			P=5*Area
				  			   		  			   			print("The perimeter of pentagon:",P)
	elif calc==3:
				  			   		  			   			Area=int(input("Enter the Area of pentagon:-"))
				  			   		  			   			perimeter=int(input("Enter the perimeter of pentagon:-"))
				  			   		  			   			l=Area*2/perimeter*5
				  			   		  			   			print("The length of pentagon:",l)
				  			   		  			   						  			   		  			   			
if option==10:
				  			   		  			   			calc=int(input("What do you want calculate\n1.Area\n2.Volume\:-"))
				  			   		  			   			if calc==1:
				  			   		  			   				radius=int(input("Enter the radius of cone:-"))
				  			   		  			   				length=int(input("Enter the length of cone:-"))
				  			   		  			   				A=22/7*length+radius
				  			   		  			   				print("The Area on cone:",A)
				  			   		  			   			elif calc==2:
				  			   		  			   									  			   		  			   			radius=int(input("Enter the radius of cone:-"))
				  			   		  			   									  			   		  			   			hight=int(input("Enter the hight of cone:-"))
				  			   		  			   									  			   		  			   			V=1/3*22/7*radius*radius*hight
				  			   		  			   									  			   		  			   			print("The Volume of cone:",V)
				  			   		  			   									  			   		  			   
				  			   		  			   									  			   		  			   			
				  			   		  			   			  			   		  			   			 
				  			   		  			   									  			   		  			   			
				  			   		  			   									  			   		  			   			
				  			   		  			   			
				  			   		  			   		