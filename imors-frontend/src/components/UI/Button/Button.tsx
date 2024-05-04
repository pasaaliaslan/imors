import React from "react";
import styles from "./Button.module.scss";

type Size = "small" | "medium" | "large";
type Variant = "primary" | "secondary" | "link" | "disabled";

type Props = {
    size?: Size;
    variant?: Variant;
    onClick?: () => void;
    children?: React.ReactNode;
};

export default function Button({ size = "medium", variant = "primary", onClick = () => {}, children }: Props) {
    return (
        <button className={`${styles[size]} ${styles[variant]}`} onClick={onClick}>
            {children}
        </button>
    );
}
