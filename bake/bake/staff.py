from flask import * 
from database import*
import uuid



staff=Blueprint('staff',__name__)

@staff.route('/staff_home')
def staff_home():
    
	return render_template('staff_home.html')


@staff.route('/staff_managestaff',methods=['post','get'])
def staff_managestaff():
	data={}
	q="select * from staff inner join login using (username)"
	res=select(q)
	
	data['staffview']=res

	if "action" in request.args:
		action=request.args['action']
		uid=request.args['uid']

		if action=='active':
			q="update login set `status`='1' where username='%s'"%(uid)
			update(q)
			q="update staff set `staff_status`='1' where username='%s'"%(uid)
			update(q)
			flash('successfully')
			return redirect(url_for('staff.staff_managestaff'))
		
		if action=='inactive':
			q="update login set `status`='0' where username='%s'"%(uid)
			update(q)
			q="update staff set `staff_status`='0' where username='%s'"%(uid)
			update(q)
			flash('successfully')
			return redirect(url_for('staff.staff_managestaff'))


		if action=='update':
			q="select * from staff where username='%s'"%(uid)
			res=select(q)
			data['staffupdate']=res

		if "update" in request.form:
			f=request.form['fname']
			l=request.form['lname']
			h=request.form['hno']
			s=request.form['street']
			g=request.form['city']
			st=request.form['state']
			p=request.form['pin']
			n=request.form['num']
			
			e=request.form['email']
			
			
			di=request.form['salary']
			
			
			
			
			q="update staff set staff_fname='%s',staff_lname='%s',staff_street='%s',staff_city='%s',staff_house_name='%s',staff_state='%s',staff_pincode='%s',staff_phone='%s',staff_email='%s',staff_salary='%s' where username='%s'"%(f,l,s,g,h,st,p,n,e,di,uid)
			update(q)
			flash('successfully')
			print(q)

			return redirect(url_for('staff.staff_managestaff'))
	

	if "staffreg" in request.form:
		f=request.form['fname']
		l=request.form['lname']
		h=request.form['hno']
		s=request.form['street']
		g=request.form['city']
		st=request.form['state']
		p=request.form['pin']
		n=request.form['num']
		
		e=request.form['email']
		
		
		di=request.form['salary']
		
		u=request.form['uname']
		pa=request.form['pwd']
		t="select * from login where username='%s'"%(u)
		val=select(t)
		if val:
				flash('already exist')

		else:
			q="insert into login values('%s','%s','staff','1')"%(u,pa)
			insert(q)
			q="insert into staff values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',curdate(),'1')"%(u,f,l,h,s,g,st,p,n,e,di)
			insert(q)
			flash('successfully')
		return redirect(url_for('staff.staff_managestaff'))


	return render_template('staff_managestaff.html',data=data)


@staff.route('/staff_managecategory',methods=['post','get'])	
def staff_managecategory():
	data={}
	q="select * from category"
	res=select(q)
	data['categoryview']=res

	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']

	else:
		action=None

	if action=='active':
		q="update category set status='1' where category_id='%s'"%(cid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managecategory'))
	if action=='inactive':
		q="update category set status='0' where category_id='%s'"%(cid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managecategory'))

	if action=='update':
		q="select * from category where category_id='%s'"%(cid)
		res=select(q)
		data['categoryupdate']=res

	if "update" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		q="update category set category_name='%s', category_description='%s' where category_id='%s'"%(f,d,cid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managecategory'))

	if "category" in request.form:
		f=request.form['fname']
		d=request.form['dis']
		t="select * from category where category_name='%s'"%(f)
		val=select(t)
		if val:
			flash('already exist')
		else:
			q="insert into category values(null,'%s','%s','1')"%(f,d)
			insert(q)
			flash('successfully')
		return redirect(url_for('staff.staff_managecategory'))
		
	return render_template('staff_managecategory.html',data=data)

@staff.route('/staff_managebrand',methods=['post','get'])
def staff_managebrand():
	data={}

	

	q="select * from brand "
	res=select(q)
	data['subview']=res

	if "action" in request.args:
		action=request.args['action']
		sid=request.args['sid']

	else:
		action=None


	if action=='active':
		q="update brand set brand_status='1' where brand_id='%s'"%(sid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managebrand'))

	if action=='inactive':
		q="update brand set brand_status='0' where brand_id='%s'"%(sid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managebrand'))

	if action=='update':
		q="select * from brand where brand_id='%s'"%(sid)
		res=select(q)
		data['brandupdate']=res


	if "update" in request.form:
	
		f=request.form['fname']
		d=request.form['dis']
		q="update brand set brand_name='%s',brand_description='%s' where brand_id='%s'"%(f,d,sid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managebrand'))

			

	if "brand" in request.form:
	
		f=request.form['fname']
		d=request.form['dis']
		t="select * from brand where brand_name='%s'"%(f)
		val=select(t)
		if val:
				flash('already exist')
		else:
			q="insert into brand values(null,'%s','%s','1')"%(f,d)
			insert(q)
			flash('successfully')
		return redirect(url_for('staff.staff_managebrand'))

	return render_template('staff_managebrand.html',data=data)

@staff.route('/staff_managecourier',methods=['post','get'])	
def staff_managecourier():
	data={}
	q="select * from courier"
	res=select(q)
	data['courierview']=res


	if "action" in request.args:
		action=request.args['action']
		vid=request.args['vid']

	else:
		action=None

	if action=='inactive':
		q="update courier set courier_status='0' where courier_id='%s'"%(vid)
		update(q)
		q="update login set `status`='0' where username='%s'"%(vid)
		update(q)
		q="SELECT * FROM  `order_master` INNER JOIN `order_details` USING (order_master_id) INNER JOIN `payment` USING (`order_master_id`) INNER JOIN `delivery` USING (order_master_id) WHERE order_status = 'assigned' AND courier_id='%s'"%(vid)
		val=select(q)
		for w in val:
			q="update order_master set order_status='paid' where order_master_id='%s'"%(w['order_master_id'])
			update(q)
			q="delete from delivery where order_master_id='%s'"%(w['order_master_id'])
			delete(q)
			# q="update courier set courier_status='1' where courier_id='%s'"%(vid)
			# update(q)
			# q="update login set `status`='0' where username='%s'"%(vid)
			# update(q)
		# q="SELECT * FROM `order_master` INNER JOIN `payment` USING (order_master_id) INNER JOIN `delivery` USING (order_master_id) INNER JOIN `courier` USING (courier_id) WHERE `courier_id` IN ( SELECT `courier_id` FROM `delivery` ) AND `order_master`.order_status <> 'Delivered'"
		# exist=select(q)
		# if exist:
		# 	flash("Cant Deactivate Couriers on Delivery")
		# else:
		# 	q="update courier set courier_Status='0' where courier_id='%s'"%(vid)
		# 	update(q)

		return redirect(url_for('staff.staff_managecourier'))

	if action=='active':
		q="update courier set courier_status='1' where courier_id='%s'"%(vid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managecourier'))

	if action=='update':
		q="select * from courier where courier_id='%s'"%(vid)
		res=select(q)
		data['courierupdate']=res

	if "up" in request.form:
		f=request.form['fname']
		n=request.form['hno']
		e=request.form['street']
		h=request.form['city']
		s=request.form['state']
		di=request.form['pin']
		p=request.form['num']
		d=request.form['email']
		
		q="update courier set courier_name='%s',courier_building_name='%s',courier_street='%s',courier_city='%s',courier_state='%s',courier_pincode='%s',courier_phone='%s',courier_email='%s' where courier_id='%s'"%(f,n,e,h,s,di,p,d,vid)
		update(q)
		flash('successfully')
		print(q)
		return redirect(url_for('staff.staff_managecourier'))
		
			

	if "courier" in request.form:
	
		f=request.form['fname']
		n=request.form['hno']
		e=request.form['street']
		h=request.form['city']
		s=request.form['state']
		di=request.form['pin']
		p=request.form['num']
		d=request.form['email']
		
		u=request.form['uname']
		pa=request.form['pwd']
		t="select * from login where username='%s'"%(u)
		val=select(t)
		if val:
				flash('already exist')

		else:
			q="insert into login values('%s','%s','courier','1')"%(u,pa)
			insert(q)
			q="insert into courier values(null,'0','%s','%s','%s','%s','%s','%s','%s','%s','%s',curdate(),'1')"%(u,f,n,e,h,s,di,p,d)
			insert(q)
			flash('successfully')
		return redirect(url_for('staff.staff_managecourier'))
	return render_template('staff_managecourier.html',data=data)



@staff.route('/staff_managevendor',methods=['post','get'])	
def staff_managevendor():
	data={}
	q="select * from vendor"
	res=select(q)
	data['vendorview']=res


	if "action" in request.args:
		action=request.args['action']
		vid=request.args['vid']

	else:
		action=None

	if action=='inactive':
		q="update vendor set vendor_status='0' where vendor_id='%s'"%(vid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managevendor'))

	if action=='active':
		q="update vendor set vendor_status='1' where vendor_id='%s'"%(vid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managevendor'))

	if action=='update':
		q="select * from vendor where vendor_id='%s'"%(vid)
		res=select(q)
		data['vendorupdate']=res

	if "up" in request.form:
		f=request.form['fname']
		n=request.form['hno']
		e=request.form['street']
		h=request.form['city']
		s=request.form['state']
		di=request.form['pin']
		p=request.form['num']
		d=request.form['email']
		
		q="update vendor set vendor_name='%s',vendor_building_name='%s',vendor_street='%s',vendor_city='%s',vendor_state='%s',vendor_pincode='%s',vendor_phone='%s',vendor_email='%s' where vendor_id='%s'"%(f,n,e,h,s,di,p,d,vid)
		update(q)
		flash('successfully')
		print(q)
		return redirect(url_for('staff.staff_managevendor'))
		
			

	if "vendor" in request.form:
	
		f=request.form['fname']
		n=request.form['hno']
		e=request.form['street']
		h=request.form['city']
		s=request.form['state']
		di=request.form['pin']
		p=request.form['num']
		d=request.form['email']
		u=request.form['uname']
		pa=request.form['pwd']
		t="select * from login where username='%s'"%(u)
		val=select(t)
		if val:
				flash('already exist')

		else:
			q="insert into login values('%s','%s','vendor','1')"%(u,pa)
			insert(q)
			q="insert into vendor values(null,'%s','0','%s','%s','%s','%s','%s','%s','%s','%s',curdate(),'1')"%(u,f,n,e,h,s,di,p,d)
			insert(q)
			flash('successfully')
		return redirect(url_for('staff.staff_managevendor'))
	return render_template('staff_managevendor.html',data=data)


@staff.route('/staff_viewbooking')
def staff_viewbooking():
	data={}
	q="SELECT * FROM `order_details` INNER JOIN `order_master` USING (`order_master_id`) INNER JOIN `product` USING (`product_id`) INNER JOIN `customer` USING (customer_id)  INNER JOIN `brand` USING (`brand_id`) INNER JOIN `category` USING (`category_id`) "
	res=select(q)
	data['bookingview']=res
	return render_template('staff_viewbooking.html',data=data)

@staff.route('/staff_viewpayment')
def staff_viewpayment():
	data={}
	oid=request.args['oid']
	q="SELECT * FROM `payment`  INNER JOIN `order_master` USING (`order_master_id`) INNER JOIN `customer` USING (`customer_id`) where order_master_id='%s'"%(oid)
	res=select(q)
	data['paymentview']=res
	return render_template('staff_viewpayment.html',data=data)


@staff.route('/staff_viewcomplaint')	
def staff_viewcomplaint():
	data={}
	q="select * from complaint inner join customer using (customer_id)"
	res=select(q)
	data['complaintview']=res
	return render_template('staff_viewcomplaint.html',data=data)

@staff.route('/staff_sendreply',methods=['post','get'])
def staff_sendreply():

	
	if "reply" in request.form:
		rep=request.form['rep']
		cid=request.args['cid']
		q="update complaint set reply='%s' where complaint_id='%s'"%(rep,cid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_viewcomplaint'))

	
	return render_template('staff_sendreply.html')	


@staff.route('/staff_viewcustomer')	
def staff_viewcustomer():
	data={}

	if "action" in request.args:
		action=request.args['action']
		lid=request.args['lid']

	else:
		action=None

	if action=='accept':
		q="update login set status='1' where username='%s'"%(lid)
		update(q)
		q="update customer set customer_status='1' where username='%s'"%(lid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_viewcustomer'))

	if action=='reject':
		q="update login set status='0' where username='%s'"%(lid)
		update(q)
		q="update customer set customer_status='0' where username='%s'"%(lid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_viewcustomer'))
			
	q="select * from customer inner join login using (username)"
	res=select(q)
	data['customerview']=res
	session['res']=res

	return render_template('staff_viewcustomer.html',data=data)

@staff.route('/staff_manageitem',methods=['post','get'])	
def staff_manageitem():
	data={}


	q="select * from brand where brand_status='1'"
	res=select(q)
	data['branddrop']=res

	q="select * from category where status='1'"
	res=select(q)
	data['catdrop']=res



	q="SELECT * FROM product INNER JOIN `brand` USING (`brand_id`)  INNER JOIN category using (category_id) "
	res=select(q)
	data['productview']=res



	if "action" in request.args:
		action=request.args['action']
		pid=request.args['pid']

	else:
		action=None

	if action=='available':
		q="update product set product_status='1' where product_id='%s'"%(pid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_manageitem'))

	if action=='notavailable':
		q="update product set product_status='0' where product_id='%s'"%(pid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_manageitem'))	

	if action=='update':
		q="SELECT * FROM product inner JOIN `brand` USING (`brand_id`) inner join category using (category_id) where product_id='%s'"%(pid)
		res=select(q)
		
		data['productupdate']=res


		if "update" in request.form:
			
			sub=request.form['brand']
			subcat=request.form['subcats']
			f=request.form['fname']
			d=request.form['dis']
			

			rate=request.form['rate']
			mfg=request.form['mfg']
			exp=request.form['exp']

			if request.files['imgg']:
				path="static/image"+str(uuid.uuid4())+i.filename
				i.save(path)
				
				q="update product set category_id='%s',brand_id='%s',product_name='%s',product_description='%s',product_image='%s',ExpiryDate='%s',ManufactureDate='%s' where product_id='%s'"%(subcat,sub,f,d,path,mfg,exp,pid)
			else:
				q="update product set category_id='%s',brand_id='%s',product_name='%s',product_description='%s' where product_id='%s'"%(subcat,sub,f,d,pid)
			update(q)
		
			# q = "SELECT * FROM purchase_child WHERE product_id = '%s'" % pid
			# res = select(q)
			# cost_price =float(res[0]['cost_price'])
			# new_profit =float(request.form['profit']) 
			# new_profit =(float(cost_price)*new_profit)/100
			# new_selling_price=int(cost_price)+int(new_profit)	
			# w="UPDATE product SET rate='%s' WHERE product_id='%s'"%(new_selling_price,pid)
			# update(w)
			# q = "UPDATE purchase_child SET selling_price = '%s' WHERE product_id = '%s'" % (new_selling_price, pid)
			# update(q)
			flash('successfully')
			return redirect(url_for('staff.staff_manageitem'))


	if "product" in request.form:
		
		sub=request.form['brand']
		subcat=request.form['subcat']
		f=request.form['fname']
		d=request.form['dis']
		i=request.files['imgg']

		rate=request.form['rate']
		mfg=request.form['mfg']
		exp=request.form['exp']

		path="static/image"+str(uuid.uuid4())+i.filename
		i.save(path)
	
		
		t="select * from product where product_name='%s'"%(f)
		val=select(t)
		if val:
				flash('already exist')
		else:
		# 	q="select * from product where product_name='%s' and product_description='%s' "%(f,d)
		# 	res=select(q)
		# if res:
		# 		alert('successfully')
		# else:

			q="insert into product values(null,'%s','%s','%s','%s','%s','0','1','%s','%s','%s')"%(sub,subcat,f,d,path,rate,mfg,exp)
			insert(q)
			flash('successfully')
			return redirect(url_for('staff.staff_manageitem'))		


	return render_template('staff_manageitem.html',data=data)


@staff.route('/staff_managepurchase',methods=['post','get'])	
def staff_managepurchase():
	data={}

	q="select * from vendor where vendor_status='1'"
	res=select(q)
	data['vendordrop']=res


	q="select * from product where product_status='1'"
	res=select(q)
	data['productdrop']=res



	q="SELECT * FROM `purchase_child` INNER JOIN `purchase_master` USING (`purchase_master_id`) INNER JOIN `vendor` USING (`vendor_id`) INNER JOIN `product` USING (`product_id`) where status='Accept'"
	res=select(q)
	data['purchaseview']=res


	if "action" in request.args:
		action=request.args['action']
		pid=request.args['pid']
	else:
		action=None

	if  action=='conform':
		q="select * from purchase_master inner join purchase_child using(purchase_master_id) where status='Accept'"
		res=select(q)
		if res:
			for i in res:
				item=i['product_id']
				S_price=i['selling_price']
				P_qty=i['quantity']
				Pur_id=i['purchase_child_id']
				
				q="select * from product where product_id='%s' and stock='0'"%(item)
				print(q)
				res1=select(q)
				if res1:
					q="update product set stock='%s',rate='%s' where  product_id='%s'"%(P_qty,S_price,item)
					update(q)
					q="update purchase_child set pc_status='stock added' where purchase_child_id='%s'"%(Pur_id)
					update(q)
					q="update purchase_master set status='paid' where purchase_master_id='%s'"%(res[0]['purchase_master_id'])
					update(q)
					q="select * from order_details where product_id='%s'"%(item)
					variable1=select(q)
					for j in variable1:
						cart_qty=j['quantity']
						q="update order_details set total_price='%s'+'%s' where product_id='%s'"%(S_price,cart_qty,item)
						update(q)
						# q="select sum(price) from tbl_cart_child inner join tbl_cart_master where Cust_id=''"
					# flash('Purchase Completed...')
				else:
					q="update purchase_master set status='paid' where purchase_master_id='%s'"%(res[0]['purchase_master_id'])
					update(q)
				# flash('Purchase Completed...')
		




		
		return redirect(url_for('staff.staff_managepurchase'))



	if "purchase" in request.form:
		ve=request.form['ven']
		p=request.form['pro']
	 
		
		qu=request.form['quantity']
		
		q="select * from product where product_id='%s'"%(p)
		c=select(q)[0]['rate']
		t=int(c)*int(qu)
		# per=int(select(q)[0]['rate'])
		# sellp= (int(c)*per)/100 	
		# new=int(c)+int(sellp)

		print(c)
		



		q="select * from purchase_master where vendor_id='%s' and status='pending'"%(ve)
		res=select(q)
		if res:
			pmid=res[0]['purchase_master_id']

		else:
			
			q="insert into purchase_master values(null,'%s','0','0','pending',curdate())"%(ve)
			pmid=insert(q)

		q="select * from purchase_child where product_id='%s' and cost_price='%s' and purchase_master_id='%s' "%(p,c,pmid)
		res=select(q)
		print(q)
		if res:

			pcid=res[0]['purchase_child_id']


			q="update purchase_child set quantity=quantity+'%s',cost_price=cost_price+'%s' where purchase_child_id='%s'"%(qu,c,pcid)
			update(q)
			print(q)

		else:


					
			q="insert into purchase_child values(null,'%s','%s','%s','%s','%s','available')"%(pmid,p,c,c,qu)
			insert(q)
			print(q)

		q="update purchase_master set total=total+'%s' where purchase_master_id='%s'"%(t,pmid)
		update(q)
		flash('successfully')

		return redirect(url_for('staff.staff_managepurchase'))


		
	
	return render_template('staff_managepurchase.html',data=data)

@staff.route('/staff_managereport',methods=['post','get'])	
def staff_managereport():
	data={}
	if "sale" in request.form:
		daily=request.form['daily']
		if request.form['monthly']=="":
			monthly=""
		else:
			monthly=request.form['monthly']+'%'
		print(monthly)
		customer=request.form['customer']	
		q="SELECT * FROM `order_details` INNER JOIN `order_master` USING (`order_master_id`) INNER JOIN `product` USING (`product_id`) INNER JOIN `customer` USING (customer_id)  INNER JOIN `brand` USING (`brand_id`) INNER JOIN `category` USING (`category_id`)  where (`customer_fname` like '%s') or (`date` like '%s'  ) or (`date` like '%s' ) "%(customer,daily,monthly)
		res=select(q)
		print(q)
		data['report']=res
		session['ress']=res
		ree=session['ress']
	else:
		q="SELECT * FROM `order_details` INNER JOIN `order_master` USING (`order_master_id`) INNER JOIN `product` USING (`product_id`) INNER JOIN `customer` USING (customer_id) INNER JOIN `brand` USING (`brand_id`)  INNER JOIN `category` USING (`category_id`)"
		res=select(q)
		data['report']=res
	
	return render_template('staff_managereport.html',data=data)

@staff.route('/staff_salesreport')
def staff_salesreport():
	data={}
	ree=session['ress']
	data['ree']=ree


	return render_template('staff_salesreport.html',data=data)	

@staff.route('/purchase_details',methods=['post','get'])
def staff_purchase_details():
    data={}
   
    
    q="select * from purchase_master inner join purchase_child using (purchase_master_id) inner join product using (product_id) inner join vendor using (vendor_id) where STATUS='paid'"
    res=select(q)
    data['purchaseview']=res
    session['res']=res
        

    
    return render_template('purchase_details.html',data=data)


@staff.route('/staff_assign',methods=['post','get'])
def	staff_assign():
    data={}
    q="select * from courier  where courier_status='1'"
    res=select(q)
    data['assignedcor']=res
    
    if "update"in request.form:
        ass=request.form['as']
        oid=request.args['oid']
        q="insert into delivery values(null,'%s','%s',curdate(),'Assigned')"%(oid,ass)
        insert(q)
        q="update order_master set order_status='Assigned' where order_master_id='%s'"%(oid)
        update(q)
        return redirect(url_for('staff.staff_viewbooking'))
    return render_template('staff_assign.html',data=data)



@staff.route('/staff_customerreport')
def staff_customerreport():
	data={}
	r=session['res']
	data['r']=r


	return render_template('staff_customerreport.html',data=data)
@staff.route('/preport')
def preport():
	data={}
	r=session['res']
	data['r']=r


	return render_template('preport.html',data=data)