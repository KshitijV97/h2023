import classNames from "classnames";

import "./Task.css";

type TaskProps = {
	title: string;
};

const STATUS = "DONE";

export const Task = ({ title }: TaskProps) => {
	return (
		<div className='task'>
			<div>{title}</div>
			<div className='bottom-wrapper'>
				<div></div>
				<div className={classNames("status", STATUS)}>{STATUS}</div>
			</div>
		</div>
	);
};
