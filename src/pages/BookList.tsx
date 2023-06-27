import { Link } from "react-router-dom";

export const BookList = () => {
	return (
		<div>
			<h1>BookList</h1>
			<Link to='/book/1'>Book 1</Link>
			<Link to='/book/2'>Book 2</Link>
		</div>
	);
};

export default BookList;
