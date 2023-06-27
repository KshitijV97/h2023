import { Column } from "../../components/Column/Column";
import "./ZustandExample.css";

export const ZustandExample = () => {
	return (
		<div className='zustand-example'>
			<Column state='PLANNED' />
			<Column state='ONGOING' />
			<Column state='DONE' />
		</div>
	);
};

export default ZustandExample;
