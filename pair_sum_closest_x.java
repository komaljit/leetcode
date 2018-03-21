import java.lang.Math;

public class scratch {
    static void printClosest(int [] input, int k){
        int r = input.length-1;
        int i = 0, res = 0, lif = 0, diff = Integer.MAX_VALUE;
        while (i<r){
            int sum = input[i] + input[r];
            if (Math.abs(sum-k)< diff){
                diff = Math.abs(sum-k);
                res = r;
                lif =  i;
            }
            else if (Math.abs(sum-k)> diff){
                break;
            }
            if (sum < k) {
                i++;
            }
            else {
                r--;
            }
        }
        System.out.println(res+" "+lif);
    }

    public static void main(String[] args) {
        scratch b = new scratch();
        int [] arr = {1,3,4,5,6,7};
        scratch.printClosest(arr,10);
    }
}

