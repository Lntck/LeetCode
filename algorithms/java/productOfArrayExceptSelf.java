class Solution {
    // 1sr Approach O(n)
    // public int[] productExceptSelf(int[] nums) {
    //     int n = nums.length;
    //     int[] result = new int[n];
    //     int[] leftProduct = new int[n];
    //     int[] rightProduct = new int[n];

    //     leftProduct[0] = 1;
    //     rightProduct[n-1] = 1;


    //     for (int i=1; i<n; i++) {
    //         leftProduct[i] = leftProduct[i-1] * nums[i-1];
    //     }

    //     for (int i=n-2; i>=0; i--) {
    //         rightProduct[i] = rightProduct[i+1] * nums[i+1];
    //     }


    //     for (int i=0; i<n; i++) {
    //         result[i] = leftProduct[i] * rightProduct[i];
    //     }

    //     return result;
    // }
    //
    // 2nd Approach O(n)
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        result[0] = 1;

        for (int i=1; i<n; i++) {
            result[i] = result[i-1] * nums[i-1];
        }

        int right = 1;
        for (int i=n-1; i>=0; i--) {
            result[i] *= right;
            right *= nums[i];

        }

        return result;
    }
}