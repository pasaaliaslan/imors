import React from "react";
import styles from './Button.module.scss';

type Size = "small" | "medium" | "large";
type Variant = "primary" | "secondary" | "link";

type Props = {
    size: Size,
    variant: Variant
}

export default function Button({...props}: Props) {
    return <button className={styles.button}></button>
}