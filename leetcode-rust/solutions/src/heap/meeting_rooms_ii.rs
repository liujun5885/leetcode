// https://leetcode-cn.com/problems/meeting-rooms-ii/

use priority_queue::PriorityQueue;

struct Solution;
impl Solution {
    pub fn min_meeting_rooms(intervals: Vec<Vec<i32>>) -> i32 {
        let mut new_intervals = intervals.to_vec();
        new_intervals.sort_by(|x, y| x[0].cmp(&y[0]));

        let mut pq = PriorityQueue::new();
        for i in new_intervals {
            if pq.is_empty() {
                pq.push(i[1], -1 * i[1]);
                continue;
            }
            if let Some(v) = pq.peek() {
                if v.0 < &i[1] {
                    pq.pop();
                }
                pq.push(i[1], -1 * i[1]);
            }
        }

        pq.len() as i32
    }
}

#[cfg(test)]
mod test {
    use crate::heap::meeting_rooms_ii::Solution;

    #[test]
    fn case01() {
        let intervals = vec![vec![0, 30], vec![5, 10], vec![15, 20]];
        let actual = Solution::min_meeting_rooms(intervals);
        let expected = 2;
        assert_eq!(actual, expected)
    }
}
