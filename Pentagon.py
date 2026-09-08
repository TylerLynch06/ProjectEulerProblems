def pent(n):
    return int(n*((3*n)-1)/2)

def isPent(x):
     return isInt((((24*x-1)**0.5)+1)/6)

def isInt(n):
    return str(float(n)).split(".")[0]=="0"

pentagons = []

count = 100000

for i in range(count): 
    pentagons.append(pent(i))
for n in range(count-1):
    for k in range(n+1,count):
        if isPent(pent(k)-pent(n)) and isPent(pent(k)+pent(n)):
            print(n,k)
print("Done")
        

using System;
using System.Collections.Generic;
					
public class Program
{
	
	public static void Main()
	{
		int count = 20000;
		double[] pentagon = new double[count];
		for (int i = 1; i<count; i++)
		{
			pentagon[i]=Pent(i);
		}
		
		double pentN = 0;
		double pentK = 0;
		
		for (int n = 1; n<count-1; n++)
		{
			for (int k = n+1; k<count; k++)
			{
				pentK=Pent(k);
				pentN=Pent(n);
				if (isPent(pentK-pentN) && isPent(pentK+pentN))
				{
					Console.WriteLine(pentK-pentN);
				}
			}							
		}
	}
	
	public static double Pent(int n)
	{
		return (n*((3*n)-1))/2;
	}
	
	public static bool isPent(double x)
	{
		double iPent = (Math.Sqrt((24*x)-1)+1)/6;
		return isInt(iPent);
	}
	
	public static bool isInt(double n)
	{
		return (n==Math.Floor(n));
	}
}
