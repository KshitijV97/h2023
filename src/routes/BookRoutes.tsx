import { Routes, Route } from "react-router-dom";
import { Book } from "../pages/Book";
import { BookList } from "../pages/BookList";
import NewBook from "../pages/NewBook";
import BookLayout from "./BookLayout";

export function BookRoutes() {
	return (
		<>
			<BookLayout />
			<Routes>
				<Route index element={<BookList />} />
				<Route path=':id' element={<Book />} />
				<Route path='new' element={<NewBook />} />
			</Routes>
		</>
	);
}
