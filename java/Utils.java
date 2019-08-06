/**
 * Copyright 2019 CoderDream's Studio
 * @Date 2019年8月6日
 * @Author scholarly
 * @Filename Utils.java
 * @Detail TODO Java 基础内容，方便刷题
 */
package com.java.base;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Stack;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.concurrent.ArrayBlockingQueue;

import javax.management.Query;

public class Utils {
	public static void main(String[] args) {
		collection();
	}
	
	public static void define() {
		int a = 0b101001;	// 以0B 或0b开头定义二进制数
		long b = 999999L;	// 以 L 结尾强制将数据转化为 long型数据
		int c = 013;	// 以 0 开头定义八进制数字
		int d = 0x13; 	// 以 0X或0x开头定义十六进制数字
		float e = 2.13e10f;	// f或F 标记数字，占 32 位
		double f = 2.13d;	// d或D 标记数字，占64位
		
		System.out.println(a);
		System.out.println(b);
		System.out.println(c);
		System.out.println(d);
		System.out.println(e);
		System.out.println(f);
		System.out.println(Long.MAX_VALUE);
		System.out.println(Float.MAX_VALUE);
		System.out.println(Double.MIN_VALUE);
		System.out.println(Integer.MAX_VALUE);
	}
	
	public static void count() {
		int a = -2>>3;	// 左移运算符
		int b = 2<<3;	// 左移运算符
		int c = 2>>3;	// 右移运算符
		int d = 2>>>3;	// 右移无符号运算符
		
		System.out.println(a);
		System.out.println(b);
		System.out.println(c);
		System.out.println(d);
	}
	
	public static void collection() {
		ArrayList<Integer> array = new ArrayList<Integer>();	// List 内容有序、重复
		array.add(2);
		array.add(1);
		System.out.println(array);
		Collections.sort(array);	// Collections.sort(array) 对 List 对象进行排序
		System.out.println(array);
		
		/**
		 * 数组定义：
		 * int[] a;
		 * int[] b = new int[3];
		 */
		int[] aint= {1, 4, 3, 4};
		System.out.println(aint[1]);
		Arrays.sort(aint);			// Arrays.sort() 对数组排序
		System.out.println(aint[1]);
		List lis = Arrays.asList(aint);	 // 固定长度的List 不可增、删
		
		Stack<ArrayList> a = new Stack<ArrayList>();	// 栈
		a.push(array);
		System.out.println(a.pop());
		
		// Set无序，内容不重复
		HashSet<Integer> set = new HashSet<>();		// HashSet 按 Hash算法查找元素，具有很好的查找和存储性s
		set.add(2);
		set.add(3);
		System.out.println(set);
		
		TreeSet<Integer> tree = new TreeSet<>();	// TreeSet 元素自动排序
		tree.add(4);
		tree.add(3);
		tree.add(2);
		System.out.println(tree);
		System.out.println(tree.lower(4));
		System.out.println(tree.subSet(2, 4));
		System.out.println(tree.headSet(2));	// 返回小于2的子集
		System.out.println(tree.tailSet(2));	// 返回大于等于2的子集
		
		// 估计用得很少
		PriorityQueue<Integer> q= new PriorityQueue<Integer>();	// 以从小到大的原则，模拟 “先进先出原则”
		q.add(12);
		System.out.println(q.peek()); 	// 获取头部信息， 不删除
		q.poll();	// 获取头部信息， 删除
		System.out.println(q.peek()); 
		
		ArrayDeque<Integer> qs = new ArrayDeque<Integer>();	// 双端队列
		qs.addFirst(12); 	// 将数组插在头部
		qs.addLast(13); 	// 将数组插在尾部
		qs.add(3);
		System.out.println(qs);
		System.out.println(qs.pop());	// 把双端队列当成栈
		qs.push(14);
		System.out.println(qs);
		
		HashMap<Integer, Integer> map = new HashMap<Integer,Integer>();		// 原理和 HashSet 相似
		map.put(1, 12);
		map.put(1, 13);
		map.put(-1, 12);
		System.out.println(map.get(1));
		System.out.println(map.get(2));
		System.out.println(map);
		
		TreeMap<Integer, Integer> tmap = new TreeMap<Integer, Integer>();	// 红黑树数据结构，根据 key 进行排序，保证集合处于有序状态；类似于 TreeSet
		tmap.put(1, 12);
		tmap.put(2, 11);
		tmap.put(-1, 1);
		System.out.println(tmap);
		
	}
}
