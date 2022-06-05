#![allow(dead_code)]

// The adult has seen it all, and can handle any drink well.
// All drinks are handled explicitly using `match`.
fn give_adult(drink: Option<&str>) {
    // Specify a course of action for each case.
    match drink {
        Some("lemonade") => println!("Yuck! Too sugary."),
        Some(inner) => println!("{}? How nice.", inner),
        None => println!("No drink? Oh well."),
    }
}

// Others will `panic` before drinking sugary drinks.
// All drinks are handled implicitly using `unwrap`.
fn drink(drink: Option<&str>) {
    // `unwrap` returns a `panic` when it receives a `None`.
    let inside = drink.unwrap();
    if inside == "lemonade" { panic!("AAAaaaaa!!!!"); }

    println!("I love {}s!!!!!", inside);
}


#[derive(Debug)]
enum Food { Apple, Carrot, Potato }

#[derive(Debug)]
struct Peeled(Food);

#[derive(Debug)]
struct Chopped(Food);

#[derive(Debug)]
struct Cooked(Food);

// Peeling food. If there isn't any, then return `None`.
// Otherwise, return the peeled food.
fn peel(food: Option<Food>) -> Option<Peeled> {
    match food {
        Some(food) => Some(Peeled(food)),
        None => None,
    }
}

// Chopping food. If there isn't any, then return `None`.
// Otherwise, return the chopped food.
fn chop(peeled: Option<Peeled>) -> Option<Chopped> {
    match peeled {
        Some(Peeled(food)) => Some(Chopped(food)),
        None => None,
    }
}

// Cooking food. Here, we showcase `map()` instead of `match` for case handling.
fn cook(chopped: Option<Chopped>) -> Option<Cooked> {
    chopped.map(|Chopped(food)| Cooked(food))
}

// A function to peel, chop, and cook food all in sequence.
// We chain multiple uses of `map()` to simplify the code.
fn process(food: Option<Food>) -> Option<Cooked> {
    food.map(|f| Peeled(f))
        .map(|Peeled(f)| Chopped(f))
        .map(|Chopped(f)| Cooked(f))
}

// Check whether there's food or not before trying to eat it!
fn eat(food: Option<Cooked>) {
    match food {
        Some(food) => println!("Mmm. I love {:?}", food),
        None => println!("Oh no! It wasn't edible."),
    }
}

#[cfg(test)]
mod test {
    use crate::introduction::option_unwrap::{chop, cook, drink, eat, Food, give_adult, peel, process};

    #[test]
    fn case_unwrap() {
        let water = Some("water");
        let lemonade = Some("lemonade");
        let void = None;

        give_adult(water);
        give_adult(lemonade);
        give_adult(void);

        let coffee = Some("coffee");
        let nothing = None;

        drink(coffee);
        let result = std::panic::catch_unwind(|| drink(nothing));
        assert!(result.is_err());
    }

    #[test]
    fn case_map() {
        let apple = Some(Food::Apple);
        let carrot = Some(Food::Carrot);
        let potato = None;

        let cooked_apple = cook(chop(peel(apple)));
        let cooked_carrot = cook(chop(peel(carrot)));
        // Let's try the simpler looking `process()` now.
        let cooked_potato = process(potato);

        eat(cooked_apple);
        eat(cooked_carrot);
        eat(cooked_potato);
    }

    #[test]
    fn case_map_1() {
        let apple = Some(Food::Apple);
        println!("{:?}", apple.map(|x| { x }));
    }
}
