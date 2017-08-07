package com.yaronp;

import java.util.ArrayList;
import java.util.List;
import java.util.ListIterator;

/**
 * Hello world!
 */
public class App {

    static void sparseArraysDistribution(List<String> theStrings, List<String> queryStrings) {

        int[] dist = new int[queryStrings.size()];
        ListIterator<String> it = theStrings.listIterator();

        while (it.hasNext()) {
            ListIterator<String> qit = queryStrings.listIterator();
            String theS = it.next();
            int i = 0;
            while(qit.hasNext()) {
                String theQ = qit.next();
                if (theS.equals(theQ)) {
                    System.out.printf("found! %s %d %s\n", theQ, i, theS);
                    dist[i] += 1;
                    break;
                }
                i++;
            }
        }

        for (int i = 0 ; i < dist.length; i++)
        {
            System.out.printf("%d ", dist[i]);
        }
    }


    public static void main(String[] args) {

        List<String> s = new ArrayList<String>();
        s.add("aba");
        s.add("baba");
        s.add("aba");
        s.add("xzxb");
        List<String> q = new ArrayList<String>();
        q.add("aba");
        q.add("xzxb");
        q.add("ab");


        App.sparseArraysDistribution(s, q);
        System.out.println("Hello World!");
    }
}
