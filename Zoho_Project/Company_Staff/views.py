from django.shortcuts import render,redirect
from Register_Login.models import *
from Company_Staff.models import *
from Register_Login.views import logout
from django.contrib import messages
from django.conf import settings
from datetime import date

from django.http import HttpResponse, HttpResponseBadRequest
from django.db.models.functions import TruncMonth,Cast, TruncDate,ExtractDay
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.db.models import Count,Sum,DurationField
from django.contrib import messages
from django.db.models import Count,Case, When, IntegerField, Q
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Count, F, Func, Value
from django.db.models.functions import TruncMonth,Extract
from django.db.models import ExpressionWrapper, fields
from calendar import month_name
from django.utils import timezone
from dateutil.relativedelta import relativedelta
# Create your views here.




# -------------------------------Company section--------------------------------

# company dashboard
def company_dashboard(request):
    if 'login_id' in request.session:
        log_id = request.session['login_id']
        if 'login_id' not in request.session:
            return redirect('/')
        log_details= LoginDetails.objects.get(id=log_id)
        dash_details = CompanyDetails.objects.get(login_details=log_details,superadmin_approval=1,Distributor_approval=1)
        allmodules= ZohoModules.objects.get(company=dash_details,status='New')

        # Calculate the date 20 days before the end date for payment term renew
        reminder_date = dash_details.End_date - timedelta(days=20)
        current_date = date.today()
        alert_message = current_date >= reminder_date

        # Calculate the number of days between the reminder date and end date
        days_left = (dash_details.End_date - current_date).days
        context = {
            'details': dash_details,
            'allmodules': allmodules,
            'alert_message':alert_message,
            'days_left':days_left,
        }
        return render(request, 'company/company_dash.html', context)
    else:
        return redirect('/')


# company staff request for login approval
def company_staff_request(request):
    if 'login_id' in request.session:
        log_id = request.session['login_id']
        if 'login_id' not in request.session:
            return redirect('/')
        log_details= LoginDetails.objects.get(id=log_id)
        dash_details = CompanyDetails.objects.get(login_details=log_details,superadmin_approval=1,Distributor_approval=1)
        allmodules= ZohoModules.objects.get(company=dash_details,status='New')
        staff_request=StaffDetails.objects.filter(company=dash_details.id, company_approval=0).order_by('-id')
        context = {
            'details': dash_details,
            'allmodules': allmodules,
            'requests':staff_request,
        }
        return render(request, 'company/staff_request.html', context)
    else:
        return redirect('/')

# company staff accept or reject
def staff_request_accept(request,pk):
    staff=StaffDetails.objects.get(id=pk)
    staff.company_approval=1
    staff.save()
    return redirect('company_staff_request')

def staff_request_reject(request,pk):
    staff=StaffDetails.objects.get(id=pk)
    login_details=LoginDetails.objects.get(id=staff.company.id)
    login_details.delete()
    staff.delete()
    return redirect('company_staff_request')


# All company staff view, cancel staff approval
def company_all_staff(request):
    if 'login_id' in request.session:
        log_id = request.session['login_id']
        if 'login_id' not in request.session:
            return redirect('/')
        log_details= LoginDetails.objects.get(id=log_id)
        dash_details = CompanyDetails.objects.get(login_details=log_details,superadmin_approval=1,Distributor_approval=1)
        allmodules= ZohoModules.objects.get(company=dash_details,status='New')
        all_staffs=StaffDetails.objects.filter(company=dash_details.id, company_approval=1).order_by('-id')
       
        context = {
            'details': dash_details,
            'allmodules': allmodules,
            'staffs':all_staffs,
        }
        return render(request, 'company/all_staff_view.html', context)
    else:
        return redirect('/')

def staff_approval_cancel(request, pk):
    """
    Sets the company approval status to 2 for the specified staff member, effectively canceling staff approval.

    This function is designed to be used for canceling staff approval, and the company approval value is set to 2.
    This can be useful for identifying resigned staff under the company in the future.

    """
    staff = StaffDetails.objects.get(id=pk)
    staff.company_approval = 2
    staff.save()
    return redirect('company_all_staff')


# company profile, profile edit
def company_profile(request):
    if 'login_id' in request.session:
        log_id = request.session['login_id']
        if 'login_id' not in request.session:
            return redirect('/')
        log_details= LoginDetails.objects.get(id=log_id)
        dash_details = CompanyDetails.objects.get(login_details=log_details,superadmin_approval=1,Distributor_approval=1)
        allmodules= ZohoModules.objects.get(company=dash_details,status='New')
        terms=PaymentTerms.objects.all()

        # Calculate the date 20 days before the end date
        reminder_date = dash_details.End_date - timedelta(days=20)
        current_date = date.today()
        renew_button = current_date >= reminder_date

        context = {
            'details': dash_details,
            'allmodules': allmodules,
            'renew_button': renew_button,
            'terms':terms,
        }
        return render(request, 'company/company_profile.html', context)
    else:
        return redirect('/')

def company_profile_editpage(request):
    if 'login_id' in request.session:
        log_id = request.session['login_id']
        if 'login_id' not in request.session:
            return redirect('/')
        log_details= LoginDetails.objects.get(id=log_id)
        dash_details = CompanyDetails.objects.get(login_details=log_details,superadmin_approval=1,Distributor_approval=1)
        allmodules= ZohoModules.objects.get(company=dash_details,status='New')
        context = {
            'details': dash_details,
            'allmodules': allmodules
        }
        return render(request, 'company/company_profile_editpage.html', context)
    else:
        return redirect('/')

def company_profile_basicdetails_edit(request):
    if 'login_id' in request.session:
        log_id = request.session['login_id']
        if 'login_id' not in request.session:
            return redirect('/')

        log_details= LoginDetails.objects.get(id=log_id)
        if request.method == 'POST':
            # Get data from the form
            log_details.first_name = request.POST.get('fname')
            log_details.last_name = request.POST.get('lname')
            log_details.email = request.POST.get('eid')
            log_details.username = request.POST.get('uname')
            log_details.save()
            messages.success(request,'Updated')
            return redirect('company_profile_editpage') 
        else:
            return redirect('company_profile_editpage') 

    else:
        return redirect('/')
    
def company_password_change(request):
    if 'login_id' in request.session:
        log_id = request.session['login_id']
        if 'login_id' not in request.session:
            return redirect('/')

        log_details= LoginDetails.objects.get(id=log_id)
        if request.method == 'POST':
            # Get data from the form
            password = request.POST.get('pass')
            cpassword = request.POST.get('cpass')
            if password == cpassword:
                log_details.password=password
                log_details.save()

            messages.success(request,'Password Changed')
            return redirect('company_profile_editpage') 
        else:
            return redirect('company_profile_editpage') 

    else:
        return redirect('/')
       
def company_profile_companydetails_edit(request):
    if 'login_id' in request.session:
        log_id = request.session['login_id']
        if 'login_id' not in request.session:
            return redirect('/')

        log_details = LoginDetails.objects.get(id=log_id)
        dash_details = CompanyDetails.objects.get(login_details=log_details,superadmin_approval=1,Distributor_approval=1)

        if request.method == 'POST':
            # Get data from the form
            gstno = request.POST.get('gstno')
            profile_pic = request.FILES.get('image')

            # Update the CompanyDetails object with form data
            dash_details.company_name = request.POST.get('cname')
            dash_details.contact = request.POST.get('phone')
            dash_details.address = request.POST.get('address')
            dash_details.city = request.POST.get('city')
            dash_details.state = request.POST.get('state')
            dash_details.country = request.POST.get('country')
            dash_details.pincode = request.POST.get('pincode')
            dash_details.pan_number = request.POST.get('pannumber')

            if gstno:
                dash_details.gst_no = gstno

            if profile_pic:
                dash_details.profile_pic = profile_pic

            dash_details.save()

            messages.success(request, 'Updated')
            return redirect('company_profile_editpage')
        else:
            return redirect('company_profile_editpage')
    else:
        return redirect('/')    

# company modules editpage
def company_module_editpage(request):
    if 'login_id' in request.session:
        log_id = request.session['login_id']
        if 'login_id' not in request.session:
            return redirect('/')
        log_details= LoginDetails.objects.get(id=log_id)
        dash_details = CompanyDetails.objects.get(login_details=log_details,superadmin_approval=1,Distributor_approval=1)
        allmodules= ZohoModules.objects.get(company=dash_details,status='New')
        context = {
            'details': dash_details,
            'allmodules': allmodules
        }
        return render(request, 'company/company_module_editpage.html', context)
    else:
        return redirect('/')

def company_module_edit(request):
    if 'login_id' in request.session:
        log_id = request.session['login_id']
        if 'login_id' not in request.session:
            return redirect('/')
        log_details= LoginDetails.objects.get(id=log_id)
        dash_details = CompanyDetails.objects.get(login_details=log_details,superadmin_approval=1,Distributor_approval=1)
        allmodules= ZohoModules.objects.get(company=dash_details,status='New')

        if request.method == 'POST':
            # Retrieve values
            items = request.POST.get('items', 0)
            price_list = request.POST.get('price_list', 0)
            stock_adjustment = request.POST.get('stock_adjustment', 0)
            godown = request.POST.get('godown', 0)

            cash_in_hand = request.POST.get('cash_in_hand', 0)
            offline_banking = request.POST.get('offline_banking', 0)
            upi = request.POST.get('upi', 0)
            bank_holders = request.POST.get('bank_holders', 0)
            cheque = request.POST.get('cheque', 0)
            loan_account = request.POST.get('loan_account', 0)

            customers = request.POST.get('customers', 0)
            invoice = request.POST.get('invoice', 0)
            estimate = request.POST.get('estimate', 0)
            sales_order = request.POST.get('sales_order', 0)
            recurring_invoice = request.POST.get('recurring_invoice', 0)
            retainer_invoice = request.POST.get('retainer_invoice', 0)
            credit_note = request.POST.get('credit_note', 0)
            payment_received = request.POST.get('payment_received', 0)
            delivery_challan = request.POST.get('delivery_challan', 0)

            vendors = request.POST.get('vendors', 0)
            bills = request.POST.get('bills', 0)
            recurring_bills = request.POST.get('recurring_bills', 0)
            vendor_credit = request.POST.get('vendor_credit', 0)
            purchase_order = request.POST.get('purchase_order', 0)
            expenses = request.POST.get('expenses', 0)
            recurring_expenses = request.POST.get('recurring_expenses', 0)
            payment_made = request.POST.get('payment_made', 0)

            projects = request.POST.get('projects', 0)

            chart_of_accounts = request.POST.get('chart_of_accounts', 0)
            manual_journal = request.POST.get('manual_journal', 0)

            eway_bill = request.POST.get('ewaybill', 0)

            employees = request.POST.get('employees', 0)
            employees_loan = request.POST.get('employees_loan', 0)
            holiday = request.POST.get('holiday', 0)
            attendance = request.POST.get('attendance', 0)
            salary_details = request.POST.get('salary_details', 0)

            reports = request.POST.get('reports', 0)

            update_action=1
            status='Pending'

            # Create a new ZohoModules instance and save it to the database
            data = ZohoModules(
                company=dash_details,
                items=items, price_list=price_list, stock_adjustment=stock_adjustment, godown=godown,
                cash_in_hand=cash_in_hand, offline_banking=offline_banking, upi=upi, bank_holders=bank_holders,
                cheque=cheque, loan_account=loan_account,
                customers=customers, invoice=invoice, estimate=estimate, sales_order=sales_order,
                recurring_invoice=recurring_invoice, retainer_invoice=retainer_invoice, credit_note=credit_note,
                payment_received=payment_received, delivery_challan=delivery_challan,
                vendors=vendors, bills=bills, recurring_bills=recurring_bills, vendor_credit=vendor_credit,
                purchase_order=purchase_order, expenses=expenses, recurring_expenses=recurring_expenses,
                payment_made=payment_made,
                projects=projects,
                chart_of_accounts=chart_of_accounts, manual_journal=manual_journal,
                eway_bill=eway_bill,
                employees=employees, employees_loan=employees_loan, holiday=holiday,
                attendance=attendance, salary_details=salary_details,
                reports=reports,update_action=update_action,status=status    
            )
            data.save()
            messages.info(request,"Request sent successfully. Please wait for approval.")
            return redirect('company_module_editpage')
        else:
            return redirect('company_module_editpage')  
    else:
        return redirect('/')


def company_renew_terms(request):
    if 'login_id' in request.session:
        log_id = request.session['login_id']
        if 'login_id' not in request.session:
            return redirect('/')
        log_details= LoginDetails.objects.get(id=log_id)
        dash_details = CompanyDetails.objects.get(login_details=log_details,superadmin_approval=1,Distributor_approval=1)
        if request.method == 'POST':
            select=request.POST['select']
            terms=PaymentTerms.objects.get(id=select)
            update_action=1
            status='Pending'
            newterms=PaymentTermsUpdates(
               company=dash_details,
               payment_term=terms,
               update_action=update_action,
               status=status 
            )
            newterms.save()
            messages.success(request,'Successfully requested an extension of payment terms. Please wait for approval.')
            return redirect('company_profile')
    else:
        return redirect('/')

def show_godown_details(request):
    godowns = Godown.objects.all()  # Retrieve all godown objects
    return render(request, 'company/show_godown_details.html', {'godowns': godowns})
def add_godown(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        item_id = request.POST.get('item')
        HSN = request.POST.get('HSN')
        stock_in_hand = request.POST.get('stock_in_hand')
        godown_name = request.POST.get('godownName')
        godown_address = request.POST.get('godownAddress')
        stock_keeping = request.POST.get('stockKeeping')
        distance = request.POST.get('kilometers')

        # Check if 'login_id' is in session
        if 'login_id' in request.session:
            # Retrieve login_id from session
            login_id = request.session['login_id']
            
            # Get the LoginDetails object
            try:
                login_details = LoginDetails.objects.get(id=login_id)
            except LoginDetails.DoesNotExist:
                # Handle the case where LoginDetails doesn't exist for the given login_id
                return HttpResponse("LoginDetails not found for the given login_id.")

            godown = Godown(
                date=date,
                item_id=item_id,
                HSN=HSN,
                stock_in_hand=stock_in_hand,
                godown_name=godown_name,
                godown_address=godown_address,
                stock_keeping=stock_keeping,
                distance=distance,
                login_details=login_details
            )
            godown.save()

            return redirect('show_godown_details')  # Redirect to the appropriate URL

        else:
            # Handle the case where 'login_id' is not in session
            return HttpResponse("Login ID not found in session. Please log in.")

    else:
        # Render the form
        items = Items.objects.all()
        context = {'items': items}
        return render(request, 'company/addgodown.html', context)
def save_item(request):
    units = Unit.objects.all()
    context = {'units': units}
    if request.method == 'POST':
        # Retrieve data from the POST request
        item_type = request.POST.get('itemType')
        item_name = request.POST.get('itemName')
        unit_id = request.POST.get('unit')  # Assuming unit is the ID of the selected unit
        hsn_code = request.POST.get('hsnCode')
        tax_reference = request.POST.get('taxReference')
        intrastate_tax = request.POST.get('intrastateTax')
        interstate_tax = request.POST.get('interstateTax')
        selling_price = request.POST.get('sellingPrice')
        sales_account = request.POST.get('salesAccount')
        sales_description = request.POST.get('salesDescription')
        purchase_price = request.POST.get('purchasePrice')
        purchase_account = request.POST.get('purchaseAccount')
        purchase_description = request.POST.get('purchaseDescription')
        minimum_stock_to_maintain = request.POST.get('minimumStockToMaintain')
        activation_tag = request.POST.get('activationTag')
        inventory_account = request.POST.get('inventoryAccount')
        opening_stock = request.POST.get('openingStock')
        opening_stock_per_unit = request.POST.get('openingStockPerUnit')
        track_inventory = request.POST.get('trackInventory')

        # Assuming 'unit' is a ForeignKey in the Items model
        unit = Unit.objects.get(pk=unit_id)

        # Create a new Items instance and save it
        item = Items(
            item_type=item_type,
            item_name=item_name,
            unit=unit,
            hsn_code=hsn_code,
            tax_reference=tax_reference,
            intrastate_tax=intrastate_tax,
            interstate_tax=interstate_tax,
            selling_price=selling_price,
            sales_account=sales_account,
            sales_description=sales_description,
            purchase_price=purchase_price,
            purchase_account=purchase_account,
            purchase_description=purchase_description,
            minimum_stock_to_maintain=minimum_stock_to_maintain,
            activation_tag=activation_tag,
            inventory_account=inventory_account,
            opening_stock=opening_stock,
            opening_stock_per_unit=opening_stock_per_unit,
            track_inventory=track_inventory
        )

        item.save()

        messages.success(request, 'Item saved successfully!')
        return redirect("/")
    else:
        messages.error(request,'Invalid request method')
        return redirect("/")
def save_unit(request):
    if request.method == 'POST':
        unit_name = request.POST.get('unitName')

        # Save the new unit
        unit = Unit(unit_name=unit_name, company=request.user.company)
        unit.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})

def add_holiday(request):
    if 'login_id' in request.session:
        log_id = request.session['login_id']
        log_details = LoginDetails.objects.get(id=log_id)

        if request.method == 'POST':
            # Check if the user is authenticated
            if not log_details:
                messages.error(request, 'You need to be logged in to add a holiday.')
                return redirect('login')

            # Retrieve data from the POST request
            holiday_name = request.POST.get('holidayName')
            start_date = request.POST.get('startDate')
            end_date = request.POST.get('endDate')
            terms_and_conditions = request.POST.get('termsAndConditions')

            # Validate the data (you may add more validation as needed)
            if not holiday_name or not start_date or not end_date or not terms_and_conditions:
                messages.error(request, 'All fields are required.')
                return render(request, 'company/addholiday.html')

            # Check if a holiday with the same date range already exists
            existing_holidays = Holiday.objects.filter(
                start_date__lte=start_date,
                end_date__gte=end_date
            )
            if existing_holidays.exists():
                messages.error(request, 'A holiday with the same date range already exists.')
                return HttpResponseBadRequest('A holiday with the same date range already exists.')

            # Save the new holiday with the logged-in user's details
            holiday = Holiday(
                holiday_name=holiday_name,
                start_date=start_date,
                end_date=end_date,
                user=log_details,
            )
            holiday.save()

            messages.success(request, 'Holiday added successfully!')
            return redirect('show_holidays')
        else:  # Handle the GET request
            user_details = {
                'user_id': log_details.id,
                'username': log_details.username,
            }
            return render(request, 'company/addholiday.html', {'user_details': user_details})
    else:
        return redirect('/')

def count_days_in_month(year, month):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29  # Leap year
        else:
            return 28  # Non-leap year
    else:
        return 30

def show_holidays(request):
    # Assuming your Holiday model has 'start_date' and 'end_date' fields
    holidays = Holiday.objects.filter(start_date__isnull=False, end_date__isnull=False).annotate(
        start_month=TruncMonth('start_date'),
        end_month=TruncMonth('end_date'),
        day_of_month=ExtractDay('start_date'),
        duration=ExpressionWrapper(F('end_date') - F('start_date'), output_field=fields.DurationField())
    ).values('start_month', 'end_month', 'day_of_month', 'duration')

    # Dictionary to keep track of cumulative counts
    cumulative_counts = {}

    for holiday in holidays:
        current_month = holiday['start_month']

        while current_month <= holiday['end_month']:
            month_year_key = (current_month.year, current_month.month)

            # Initialize remaining_days_in_second_month for each month
            remaining_days_in_second_month = 0

            if holiday['duration'].days == 0:  # Check if start date and end date are the same
                working_days = count_days_in_month(current_month.year, current_month.month) - 1
                holidays_count = 1
            else:
                # Calculate the number of days in the current month affected by the holiday
                start_day = max(holiday['day_of_month'], 1)  # Ensure start_day is at least 1
                end_day = min(start_day + holiday['duration'].days - 1, count_days_in_month(current_month.year, current_month.month))
                affected_days = max(end_day - start_day + 1, 0)

                if current_month == holiday['start_month']:
                    # Adjust affected days for the first month
                    affected_days = min(affected_days, count_days_in_month(current_month.year, current_month.month) - holiday['day_of_month'] + 1)

                # Calculate the remaining days in the second month
                remaining_days_in_second_month = holiday['duration'].days - affected_days

                working_days = count_days_in_month(current_month.year, current_month.month) - affected_days
                holidays_count = affected_days

            if month_year_key in cumulative_counts:
                # Update cumulative counts
                cumulative_counts[month_year_key]['working_days'] += working_days - holidays_count
                cumulative_counts[month_year_key]['remaining_days_in_second_month'] += remaining_days_in_second_month
                cumulative_counts[month_year_key]['holidays'] += holidays_count
            else:
                # Add new entry in the dictionary
                cumulative_counts[month_year_key] = {
                    'working_days': working_days,
                    'holidays': holidays_count,
                    'remaining_days_in_second_month': remaining_days_in_second_month,
                }

            # Move to the next month using relativedelta
            current_month = (current_month + relativedelta(months=1)).replace(day=1)

    # Debugging output
    print(cumulative_counts)

    # Convert dictionary values to a list for rendering
    context={'holidays': [{'month': key[1], 'year': key[0], **value, 'total_days': count_days_in_month(key[0], key[1])} for key, value in cumulative_counts.items()]}
    return render(request, 'company/showholiday.html', context)


# -------------------------------Staff section--------------------------------

# staff dashboard
def staff_dashboard(request):
    if 'login_id' in request.session:
        log_id = request.session['login_id']
        if 'login_id' not in request.session:
            return redirect('/')
        log_details= LoginDetails.objects.get(id=log_id)
        dash_details = StaffDetails.objects.get(login_details=log_details,company_approval=1)
        allmodules= ZohoModules.objects.get(company=dash_details.company,status='New')
        context={
            'details':dash_details,
            'allmodules': allmodules,
        }
        return render(request,'staff/staff_dash.html',context)
    else:
        return redirect('/')


# staff profile
def staff_profile(request):
    if 'login_id' in request.session:
        log_id = request.session['login_id']
        if 'login_id' not in request.session:
            return redirect('/')
        log_details= LoginDetails.objects.get(id=log_id)
        dash_details = StaffDetails.objects.get(login_details=log_details,company_approval=1)
        allmodules= ZohoModules.objects.get(company=dash_details.company,status='New')
        context={
            'details':dash_details,
            'allmodules': allmodules,
        }
        return render(request,'staff/staff_profile.html',context)
    else:
        return redirect('/')


def staff_profile_editpage(request):
    if 'login_id' in request.session:
        log_id = request.session['login_id']
        if 'login_id' not in request.session:
            return redirect('/')
        log_details= LoginDetails.objects.get(id=log_id)
        dash_details = StaffDetails.objects.get(login_details=log_details,company_approval=1)
        allmodules= ZohoModules.objects.get(company=dash_details.company,status='New')
        context = {
            'details': dash_details,
            'allmodules': allmodules
        }
        return render(request, 'staff/staff_profile_editpage.html', context)
    else:
        return redirect('/')

def staff_profile_details_edit(request):
    if 'login_id' in request.session:
        log_id = request.session['login_id']
        if 'login_id' not in request.session:
            return redirect('/')

        log_details= LoginDetails.objects.get(id=log_id)
        dash_details = StaffDetails.objects.get(login_details=log_details,company_approval=1)
        if request.method == 'POST':
            # Get data from the form
            log_details.first_name = request.POST.get('fname')
            log_details.last_name = request.POST.get('lname')
            log_details.email = request.POST.get('eid')
            log_details.username = request.POST.get('uname')
            log_details.save()
            dash_details.contact = request.POST.get('phone')
            old=dash_details.image
            new=request.FILES.get('profile_pic')
            print(new,old)
            if old!=None and new==None:
                dash_details.image=old
            else:
                print(new)
                dash_details.image=new
            dash_details.save()
            messages.success(request,'Updated')
            return redirect('staff_profile_editpage') 
        else:
            return redirect('staff_profile_editpage') 

    else:
        return redirect('/')

def staff_password_change(request):
    if 'login_id' in request.session:
        log_id = request.session['login_id']
        if 'login_id' not in request.session:
            return redirect('/')

        log_details= LoginDetails.objects.get(id=log_id)
        if request.method == 'POST':
            # Get data from the form
            password = request.POST.get('pass')
            cpassword = request.POST.get('cpass')
            if password == cpassword:
                log_details.password=password
                log_details.save()

            messages.success(request,'Password Changed')
            return redirect('staff_profile_editpage') 
        else:
            return redirect('staff_profile_editpage') 

    else:
        return redirect('/')






# -------------------------------Zoho Modules section--------------------------------
