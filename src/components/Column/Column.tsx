import "./Column.css";
import { Task } from "../Task/Task";

type ColumnProps = {
	state: string;
};

export const Column = ({ state }: ColumnProps) => {
	return (
		<div className='column'>
			<p>{state}</p>
			<Task title='Todo' />
		</div>
	);
};
