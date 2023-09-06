// https://leetcode.cn/problems/implement-stack-using-queues/

struct MyStack {
    queue: Vec<i32>,
}

impl MyStack {
    fn new() -> Self {
        Self { queue: vec![] }
    }

    fn push(&mut self, x: i32) {
        self.queue.push(x);
    }

    fn pop(&mut self) -> i32 {
        self.queue.pop().unwrap()
    }

    fn top(&self) -> i32 {
        *self.queue.last().unwrap()
    }

    fn empty(&self) -> bool {
        self.queue.is_empty()
    }
}

#[cfg(test)]
mod test {
    use super::MyStack;

    #[test]
    fn case01() {
        let mut stack = MyStack::new();
        stack.push(1);
        stack.push(2);
        assert_eq!(2, stack.top());
        assert_eq!(2, stack.pop());
        assert_eq!(1, stack.top());
        assert_eq!(1, stack.pop());
        assert_eq!(true, stack.empty());
    }
}
