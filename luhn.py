class Luhn:

    def pass_luhn(self, acct):
        sum = 0
        qualified = False
        if(acct.isnumeric()):
            qualified = True
        if(qualified==False):
            return False
        if(qualified):
            sum+=int(acct[len(acct)-1])
            for x in range (len(acct)-2, -1, -2):
                if(x!=0):
                    sum+=int(acct[x-1:x])
                num = int(acct[x:x+1])*2
                if(num<10):
                    sum+=num
                else:
                    sum+= num-9
        
            
        """
        if(sum%10==0):
            print(acct+ " passed: sum: " + str(sum) + " mod: " + str(sum%10))
        """
        ret = sum%10==0
        return (ret)
    
    def is_amex(self, acct):
        if(self.pass_luhn(acct)):
            if(len(acct)==15 and (acct[0:2]=="34" or acct[0:2]=="37")):
                return True
        return False

    def is_visa(self, acct):
        if(not self.pass_luhn(acct)):
            return False
        if((len(acct)==13 or len(acct)==16) and acct[0]=="4"):
            return True
        return False

    def is_mastercard(self, acct):
        if(not self.pass_luhn(acct)):
            return False
        if(len(acct)==16 and (acct[0:2]=="51" or acct[0:2]=="52" or acct[0:2]=="53"  or acct[0:2]=="54" or acct[0:2]=="55")):
            return True
        return False

    def is_discover(self, acct):
        if(not self.pass_luhn(acct)):
            return False
        if(len(acct)==16 and acct[0:4]=="6011"):
            return True
        return False

    def is_valid_cc(self, acct):
        if(self.is_visa(acct) or self.is_amex(acct) or self.is_mastercard(acct) or self.is_discover(acct)):
            return True
        return False