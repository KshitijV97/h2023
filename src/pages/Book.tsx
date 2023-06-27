import { useParams } from "react-router-dom";

export const Book = () => {
	const { id } = useParams();
	return (
		<div>
			<h1>You are on Book {id}</h1>
		</div>
	);
};

export default Book;
