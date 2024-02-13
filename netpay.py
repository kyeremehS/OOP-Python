class NetPay():
    """A model to calculate the net pay of employees"""
    def __init__(self,hours_worked,gender, num_children,child_gender):
        """Initializing hours worked and gender"""
        self.hours_worked = hours_worked
        self.gender = gender
        self.num_children = num_children
        self.child_gender = child_gender

    def gross_pay(self):
        """Calculate the gross pay of employees"""
    
        if self.hours_worked <= 40:
            if self.gender == 'male':
                gross_pay = self.hours_worked * 500
            else:
                gross_pay = self.hours_worked * 550
        else:
            overtime = self.hours_worked - 40
            if self.gender == 'male':
                gross_pay = (overtime * 750) + 40 * 500
            else:
                gross_pay = (overtime  * 825) + 40 * 550
        print(f"Gross pay: {gross_pay}")

    def eduFund(self):
        """Calculate the cost for EduFund"""
        if self.num_children <= 3:
            eduFund = 0
        else:
            if self.child_gender == 'male':
                eduFund = (self.num_children - 3) * 10
            else:
                eduFund = (self.num_children - 3) * 20
        print(f'Educational Contribution is ${eduFund}')


    def Taxes(self,gross_pay):
        """Calculate taxes of employees."""
        incomeTax = 0.15 * gross_pay
        NHCLevy = 0.025 * gross_pay
        districtTax = 0.01 * gross_pay
        totalTax = incomeTax + NHCLevy + districtTax
        print(f'{totalTax}')



employee1 = NetPay(42, 'male', 5, 'male' )
employee1.gross_pay()
employee1.eduFund()
employee1.Taxes(21500)

        