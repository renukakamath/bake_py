from flask import *
from database import*

courier=Blueprint('courier',__name__)

@courier.route('/courier_home')
def courier_home():

	return render_template('courier_home.html')

@courier.route('/courier_viewbookings')
def courier_viewbookings():
	data={}
	cid=session['courier_id']

	if "action" in request.args:
		action=request.args['action']
		oid=request.args['oid']
	else:
		action=None

	if action=='picked':
		q="update order_master set order_status='Picked' where order_master_id='%s'"%(oid)
		update(q)
		flash('successfully')
		return redirect(url_for('courier.courier_viewbookings'))

	if action=='Delivered':

		q="insert into delivery values(null,'%s','%s',curdate(),'Delivered')"%(oid,cid)
		insert(q)
		q="update order_master set order_status='Delivered' where order_master_id='%s'"%(oid)
		update(q)
		flash('successfully')
		return redirect(url_for('courier.courier_viewbookings'))

			
	q="select * FROM `order_details` INNER JOIN `order_master` USING (`order_master_id`) INNER JOIN `product` USING (`product_id`) INNER JOIN `customer` USING (`customer_id`)  INNER JOIN delivery USING (order_master_id)   inner join brand using (brand_id)inner join category using (category_id)  where (courier_id='%s' and order_status='paid') or (courier_id='%s' and order_status='Picked') or (courier_id='%s' and order_status='Delivered')  or (courier_id='%s' and order_status='Assigned') "%(cid,cid,cid,cid)
	# q="select * FROM `order_details` INNER JOIN `order_master` USING (`order_master_id`) INNER JOIN `product` USING (`product_id`) INNER JOIN `customer` USING (`customer_id`)   inner join subcategory using (subcategory_id) inner join category using (category_id)  where order_status='paid' or  order_status='Picked or  order_status='Delivered' or order_status='Assigned' and  courier_id='%s' "%(cid)
	res=select(q)
	data['book']=res

	return render_template('courier_viewbookings.html',data=data)	


@courier.route('/Viewuserdetails')	
def Viewuserdetails():
	data={}
	oid=request.args['oid']

	
			
	q="select * from order_master inner join customer using (customer_id) where order_master_id='%s'"%(oid)
	res=select(q)
	data['customerview']=res
	

	return render_template('Viewuserdetails.html',data=data)


	