package com.yaronp;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

import java.util.Arrays;

/**
 * Unit test for simple App.
 */
public class AppTest
        extends TestCase {
    /**
     * Create the test case
     *
     * @param testName name of the test case
     */
    public AppTest(String testName) {
        super(testName);
    }

    /**
     * @return the suite of tests being tested
     */
    public static Test suite() {
        return new TestSuite(AppTest.class);
    }

    /**
     * Rigourous Test :-)
     */
    public void testApp() {
        int n = 4;
        int[] a = { 1, 4, 3, 2 };
        int[] na = Solution.reverseArray(a, n);
        int[] nar = {2, 3, 4, 1};
        assertTrue(Arrays.equals(na, nar));
    }
}
