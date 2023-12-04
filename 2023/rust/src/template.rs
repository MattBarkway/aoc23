use crate::utils::types::SimpleResult;

pub fn pt_1<T: AsRef<str>>(lines: &[T]) -> SimpleResult<()> {
    Ok(())
}

pub fn pt_2<T: AsRef<str>>(lines: &[T]) -> SimpleResult<()> {
    Ok(())
}

#[cfg(test)]
mod tests {
    use crate::utils::types::SimpleResult;
    use super::*;

    #[test]
    fn test_pt_1() -> SimpleResult<()> {
        let input = "";
        let as_lines = input.lines().collect::<Vec<&str>>();

        assert_eq!((), pt_1(&as_lines)?);
        Ok(())
    }

    #[test]
    fn test_pt_2() -> SimpleResult<()> {
        let input = "";

        let as_lines = input.lines().collect::<Vec<&str>>();
        assert_eq!((), pt_2(&as_lines)?);
        Ok(())
    }
}
