import { Link, Outlet } from "react-router-dom";

export const BookLayout = () => {
	return (
		<>
			<Link to='/books/1'>Book 1</Link> <br />
			<Link to='/books/2'>Book 2</Link> <br />
			<Link to='/books/new'>New book</Link> <br />
			<Outlet />
		</>
	);
};

export default BookLayout;
