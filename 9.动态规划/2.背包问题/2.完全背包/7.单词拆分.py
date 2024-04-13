#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :7.单词拆分.py
# @Time     :2022/3/24 下午3:18
# @Author   :Chang Qing
 
"""
leetcode 139
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1： 输入: s = "leetcode", wordDict = ["leet", "code"] 输出: true 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2： 输入: s = "applepenapple", wordDict = ["apple", "pen"] 输出: true 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。   注意你可以重复使用字典中的单词。
示例 3： 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"] 输出: false

思路：
动规五部曲分析如下：

1.确定dp数组以及下标的含义
dp[i] : 字符串长度为i的话，dp[i]为true，表示可以拆分为一个或多个在字典中出现的单词。

2.确定递推公式
如果确定dp[j] 是true，且 [j, i] 这个区间的子串出现在字典里，那么dp[i]一定是true。（j < i ）。
所以递推公式是 if([j, i] 这个区间的子串出现在字典里 && dp[j]是true) 那么 dp[i] = true。
3.dp数组如何初始化
从递归公式中可以看出，dp[i] 的状态依靠 dp[j]是否为true，那么dp[0]就是递归的根基，dp[0]一定要为true，否则递归下去后面都都是false了。
那么dp[0]有没有意义呢？
dp[0]表示如果字符串为空的话，说明出现在字典里。
但题目中说了“给定一个非空字符串 s” 所以测试数据中不会出现i为0的情况，那么dp[0]初始为true完全就是为了推导公式。
下标非0的dp[i]初始化为false，只要没有被覆盖说明都是不可拆分为一个或多个在字典中出现的单词。

4.确定遍历顺序
题目中说是拆分为一个或多个在字典中出现的单词，所以这是完全背包。
还要讨论两层for循环的前后循序。
如果求组合数就是外层for循环遍历物品，内层for遍历背包。
如果求排列数就是外层for遍历背包，内层for循环遍历物品。
本题最终要求的是是否都出现过，所以对出现单词集合里的元素是组合还是排列，并不在意！
那么本题使用求排列的方式，还是求组合的方式都可以。
但本题还有特殊性，因为是要求子串，最好是遍历背包放在外循环，将遍历物品放在内循环。
如果要是外层for循环遍历物品，内层for遍历背包，就需要把所有的子串都预先放在一个容器里。（如果不理解的话，可以自己尝试这么写一写就理解了）
所以最终我选择的遍历顺序为：遍历背包放在外循环，将遍历物品放在内循环。内循环从前到后。

5.举例推导dp[i]
单词就是物品，字符串s就是背包，单词能否组成字符串s，就是问物品能不能把背包装满。

https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0139.%E5%8D%95%E8%AF%8D%E6%8B%86%E5%88%86.md
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''排列'''
        dp = [False]*(len(s) + 1)
        dp[0] = True
        # 遍历背包
        for j in range(1, len(s) + 1):
            # 遍历单词
            for word in wordDict:
                if j >= len(word):
                    dp[j] = dp[j] or (dp[j - len(word)] and word == s[j - len(word):j])
        return dp[len(s)]


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''排列'''
        dp = [False]*(len(s) + 1)
        dp[0] = True
        # 遍历背包
        for word in wordDict:

            for j in range(len(word), len(s) + 1):
            # 遍历单词
                dp[j] = dp[j] or (dp[j - len(word)] and word == s[j - len(word):j])
        return dp[len(s)]
"""
回溯法：
class Solution {
private:
    bool backtracking (const string& s,
            const unordered_set<string>& wordSet,
            vector<bool>& memory,
            int startIndex) {
        if (startIndex >= s.size()) {
            return true;
        }
        // 如果memory[startIndex]不是初始值了，直接使用memory[startIndex]的结果
        if (!memory[startIndex]) return memory[startIndex];
        for (int i = startIndex; i < s.size(); i++) {
            string word = s.substr(startIndex, i - startIndex + 1);
            if (wordSet.find(word) != wordSet.end() && backtracking(s, wordSet, memory, i + 1)) {
                return true;
            }
        }
        memory[startIndex] = false; // 记录以startIndex开始的子串是不可以被拆分的
        return false;
    }
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
        vector<bool> memory(s.size(), 1); // -1 表示初始化状态
        return backtracking(s, wordSet, memory, 0);
    }
};
"""

