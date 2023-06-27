import "./App.css";
import { Link, Routes, Route } from "react-router-dom";
import { Home } from "./pages/Home";
import { Book } from "./pages/Book";
import { BookList } from "./pages/BookList";
import { NotFound } from "./pages/NotFound";
import NewBook from "./pages/NewBook";

function App() {
	return (
		<div>
			<h1 className='text-3xl font-bold underline text-center'>Hello world!</h1>
			<nav>
				<ul>
					<li>
						<Link to='/'>Home</Link>
					</li>
					<li>
						<Link to='/books'>Books</Link>
					</li>
				</ul>
			</nav>
			<Routes>
				<Route path='/' element={<Home />} />
				<Route path='/books' element={<BookList />} />
				<Route path='/book/:id' element={<Book />} />
				<Route path='/book/new' element={<NewBook />} />
				<Route path='*' element={<NotFound />} />
			</Routes>
		</div>
	);
}

export default App;
