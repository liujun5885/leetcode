package com.aa.charles;

/**
 * leetcode 493
 */
class lc493 {

    private int count(int[] nums, int left, int right) {
        //退出条件当left == right时候两个数变成一个数不满足题目要求
        if (left >= right) {
            return 0;
        }
        int mid = left + (right - left) / 2;
        //先计算两边单独的满足要求的i和j
        int r = count(nums, left, mid) + count(nums, mid + 1, right);
        //这里的temp是将nums[left~right]之间的排好序的临时数组
        int[] temp = new int[right - left + 1];
        //i, j是用来进行merge sort所用到的，k代表temp中的下标，t代表从右边数组开始所有满足题意的j
        //这里有一个关键需要理解的就是在进入这个for之前，left和right两边已经是有序的了，因为之前count了left和right所有他们是有序的
        for (int i = left, j = mid + 1, k = 0, t = j; k < temp.length; ++k) {
            //这里的if条件其实是为merge sort准备的，表示要将左边数组下标i的数放入temp中的条件
            //i必须没有到达左边数组的右边界并且右边数组满足要求
            if (i <= mid && (j > right || nums[i] < nums[j])) {
                //t是持续单增的，不会后退，因为当i增大的时候t一定会变得更大(left和right数组都是有序的)， for循环找到满足条件的右边界获取到i j在左右的数量
                for (; t <= right && nums[i] > 2L * nums[t]; ++t);
                r += t - mid - 1;
                //merge sort
                temp[k] = nums[i++];
            } else {
                //merge sort
                temp[k] = nums[j++];
            }
        }
        //将排好序的数组放入原数组
        for (int i = left; i <= right; ++i) {
            nums[i] = temp[i - left];
        }

        return r;
    }
    public int reversePairs(int[] nums) {
        return count(nums, 0, nums.length - 1);
    }
}
