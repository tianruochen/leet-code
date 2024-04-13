#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :6.跳跃游戏II.py
# @Time     :2022/3/4 下午3:19
# @Author   :Chang Qing
 


"""
leetcode 45
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明: 假设你总是可以到达数组的最后一个位置。

解析：
如果我们「贪心」地进行正向查找，每次找到可到达的最远位置，就可以在线性时间内得到最少的跳跃次数。

例如，对于数组 [2,3,1,2,4,2,3]，初始位置是下标 0，从下标 0 出发，最远可到达下标 2。下标 0 可到达的位置中，下标 1 的值是 3，从下标 1 出发可以达到更远的位置，因此第一步到达下标 1。

从下标 1 出发，最远可到达下标 4。下标 1 可到达的位置中，下标 4 的值是 4 ，从下标 4 出发可以达到更远的位置，因此第二步到达下标 4。

在具体的实现中，我们维护当前能够到达的最大下标位置，记为边界。我们从左到右遍历数组，到达边界时，更新边界并将跳跃次数增加 1。

在遍历数组时，我们不访问最后一个元素，这是因为在访问最后一个元素之前，我们的边界一定大于等于最后一个位置，否则就无法跳到最后一个位置了。如果访问最后一个元素，在边界正好为最后一个位置的情况下，我们会增加一次「不必要的跳跃次数」，因此我们不必访问最后一个元素。
————————————————
原文链接：https://blog.csdn.net/weixin_42120561/article/details/114194952
"""


class Solution:
    def jump(self, nums):
        max_pos = 0
        end = 0  # 边界
        count = 0   # 步数
        for i in range(len(nums) -1):
            max_pos = max(max_pos, nums[i] + i)
            if i == end:
                end = max_pos
                count += 1
        return count


"""
// 版本一
class Solution {
public:
    int jump(vector<int>& nums) {
        if (nums.size() == 1) return 0;
        int curDistance = 0;    // 当前覆盖最远距离下标
        int ans = 0;            // 记录走的最大步数
        int nextDistance = 0;   // 下一步覆盖最远距离下标
        for (int i = 0; i < nums.size(); i++) {
            nextDistance = max(nums[i] + i, nextDistance);  // 更新下一步覆盖最远距离下标
            if (i == curDistance) {                         // 遇到当前覆盖最远距离下标
                if (curDistance != nums.size() - 1) {       // 如果当前覆盖最远距离下标不是终点
                    ans++;                                  // 需要走下一步
                    curDistance = nextDistance;             // 更新当前覆盖最远距离下标（相当于加油了）
                    if (nextDistance >= nums.size() - 1) break; // 下一步的覆盖范围已经可以达到终点，结束循环
                } else break;                               // 当前覆盖最远距离下标是集合终点，不用做ans++操作了，直接结束
            }
        }
        return ans;
    }
};
"""



# 回溯 会超时
"""
//backtracking
public class Solution {
	
	int steps;
 
	public int jump(int[] nums) {
        int n = nums.length;
        steps = n - 1;
        
        jump(nums, 0, 0);
        
        return steps;
    }
	private void jump(int[] nums, int index, int tempSteps) {
		if(index >= nums.length - 1) {
			if(index == nums.length - 1) {
				steps = Math.min(steps, tempSteps);
			}
			return;
		}
		for (int i = 1; i <= nums[index]; i++) {
			jump(nums, index + i, tempSteps + 1);
		}
	}
}"""

