fn add_one(x: i32) -> i32 {
    x + 1
}

fn do_twice(f: fn(i32) -> i32, arg: i32) -> i32 {
    f(arg) + f(arg)
}

#[cfg(test)]
mod test {
    use crate::introduction::closure::{add_one, do_twice};

    #[test]
    fn case01() {
        let answer = do_twice(add_one, 5);
        assert_eq!(answer, 12);

        let list_of_numbers = vec![1, 2, 3];
        let list_of_strings_v1: Vec<String> = list_of_numbers
            .iter()
            .map(ToString::to_string)
            .collect();
        let list_of_strings_v2: Vec<String> = list_of_numbers
            .iter()
            .map(ToString::to_string)
            .collect();
        assert_eq!(list_of_strings_v1, list_of_strings_v2)
    }
}