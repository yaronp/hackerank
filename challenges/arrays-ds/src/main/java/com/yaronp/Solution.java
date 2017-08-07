package com.yaronp;

import java.util.Scanner;

public class Solution {

    public static int[] reverseArray(int arr[], int n) {
        int new_arr[] = new int[n];
        for (int i = 0; i < n; i++)
            new_arr[n-i-1] = arr[i];
        return new_arr;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int arr[] = new int[n];
        for (int arr_i = 0; arr_i < n; arr_i++) {
            arr[arr_i] = in.nextInt();
        }
        int[] na = reverseArray(arr, n);
        for (int i = n; i > 0; i--)
            System.out.printf("%d%s", na[i - 1], (i == 0 ? "" : " "));
    }
}
