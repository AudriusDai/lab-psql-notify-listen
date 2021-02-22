CREATE TABLE public.order
(
    id serial PRIMARY KEY,
    name VARCHAR (50) NOT NULL,
    description VARCHAR NULL,
    created_on TIMESTAMP NOT NULL
);


CREATE OR REPLACE FUNCTION public.notify() RETURNS trigger AS
$BODY$
BEGIN
    PERFORM pg_notify('myEvent', row_to_json(NEW)::text);
    RETURN new;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE COST 100;


CREATE TRIGGER order_after
AFTER INSERT
ON public.order
FOR EACH ROW
EXECUTE PROCEDURE public.notify();

INSERT INTO public.order(name, description, created_on)
VALUES ('The name', 'Description it is!', '2004-10-19 10:23:54')