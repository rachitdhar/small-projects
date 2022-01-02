import React, { useState, useRef, useEffect } from 'react';

function TodoForm(props) {
    const [input, setInput] = useState(props.edit ? props.edit.value : '');

    // inputRef and useEffect are for keeping focus on the textbox always
    const inputRef = useRef(null);

    useEffect(() => {
        inputRef.current.focus();
    });

    const handleChange = e => {
        setInput(e.target.value);
    };

    const handleSubmit = e => {
        e.preventDefault(); // to prevent refresh every time button is pressed

        props.onSubmit({
            id: Math.floor(Math.random() * 10000),
            text: input
        });

        setInput('');
    };

    return (
        <form className='todo-form' onSubmit={handleSubmit}>
            {props.edit ? (
                <>
                    <input
                        type='text'
                        placeholder='Update your item'
                        value={input}
                        className='todo-input edit'
                        name='text'
                        onChange={handleChange}
                        ref={inputRef}
                    >
                    </input>
                    <button className='todo-button edit'>Update</button>
                </>
            ) : (
                <>
                    <input 
                        type='text' 
                        placeholder='Add a todo'
                        value={input}
                        name='text'
                        className='todo-input'
                        onChange={handleChange}
                        ref={inputRef}
                    />
                    <button className='todo-button'>Add todo</button>                
                </>
            )}
        </form>
    )
}

export default TodoForm;