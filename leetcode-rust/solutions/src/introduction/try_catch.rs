macro_rules! attempt { // `try` is a reserved keyword
   (@recurse ($a:expr) { } catch ($e:ident) $b:block) => {
      if let Err ($e) = $a $b
   };
   (@recurse ($a:expr) { $e:expr; $($tail:tt)* } $($handler:tt)*) => {
      attempt!{@recurse ($a.and_then (|_| $e)) { $($tail)* } $($handler)*}
   };
   ({ $e:expr; $($tail:tt)* } $($handler:tt)*) => {
      attempt!{@recurse ($e) { $($tail)* } $($handler)* }
   };
}

#[derive(Debug)]
enum MyError {
    DoStep1Error,
    DoStep2Error,
    DoStep3Error,
}


fn do_step1() -> Result<(), MyError> {
    println!("Step 1");
    Ok(())
}

fn do_step2() -> Result<(), MyError> {
    println!("Step 2");
    Err(MyError::DoStep2Error)
}

fn do_step3() -> Result<(), MyError> {
    println!("Step 3");
    Ok(())
}


#[cfg(test)]
mod test {
    use crate::introduction::try_catch::{do_step1, do_step2, do_step3, MyError};

    #[test]
    fn test1() {
        attempt! {{
            do_step1();
            do_step2();
            do_step3();
        } catch (e) {
            println!("Failed to perform necessary steps: {:?}", e);
        }}
    }

    #[test]
    fn test2() {
        let do_steps = || -> Result<(), MyError> {
            do_step1()?;
            do_step2()?;
            do_step3()?;
            Ok(())
        };

        if let Err(_err) = do_steps() {
            println!("Failed to perform necessary steps: {:?}", _err);
        }
    }
}